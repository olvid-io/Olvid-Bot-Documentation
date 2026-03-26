import os
import re
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Any, Set, Union, Optional
from google.protobuf.descriptor_pb2 import FileDescriptorSet

# --- CONFIGURATION ---
PREFERRED_FILES: List[str] = [
	"message", "attachment", "discussion", "contact", "group",
	"identity", "client_key", "invitation", "settings", "storage", "discussionstorage",
	"keycloak", "call", "backup"
]

PROTO_TYPES: Dict[int, str] = {
	1: "double", 2: "float", 3: "int64", 4: "uint64", 5: "int32",
	6: "fixed64", 7: "fixed32", 8: "bool", 9: "string", 11: "message",
	12: "bytes", 13: "uint32", 14: "enum", 15: "sfixed32",
	16: "sfixed64", 17: "sint32", 18: "sint64"
}

# --- DATA MODELS ---
# These dataclasses replace the giant nested dictionaries, providing
# clear schemas for the data extracted from the Protobuf files.

@dataclass
class ParsedEnumValue:
	name: str
	number: int
	desc: str

@dataclass
class ParsedEnum:
	name: str
	full_type: str
	desc: str
	line: int
	file: "ParsedFile"
	values: Dict[str, ParsedEnumValue] = field(default_factory=dict)

	@property
	def type(self) -> str:
		return "enum"

@dataclass
class ParsedField:
	name: str
	type: str
	full_type: str
	is_scalar: bool
	is_enum: bool
	is_message: bool
	is_repeated: bool
	is_optional: bool
	desc: str
	is_deprecated: bool
	message: Optional["ParsedMessage"] = None
	enum: Optional["ParsedEnum"] = None

@dataclass
class ParsedOneofField:
	name: str
	subfields: list["ParsedField"]
	is_repeated: bool
	desc: str
	is_deprecated: bool

@dataclass
class ParsedMessage:
	name: str # IdentitySettings.AutoAcceptInvitation
	full_type: str # example: 'olvid.daemon.datatypes.v1.IdentitySettings.AutoAcceptInvitation'
	desc: str
	line: int
	file: "ParsedFile"
	fields: List[ParsedField|ParsedOneofField] = field(default_factory=list)

	@property
	def type(self) -> str:
		return "message"

@dataclass
class ParsedRPC:
	name: str
	desc: str
	input_name: str
	output_name: str
	client_streaming: bool
	server_streaming: bool
	input: ParsedMessage = None
	output: ParsedMessage = None

@dataclass
class ParsedService:
	name: str
	datatype: str
	desc: str
	file: "ParsedFile"
	rpcs: Dict[str, ParsedRPC] = field(default_factory=dict)

@dataclass
class ParsedFile:
	filename: str # ex: message.proto
	filepath: str # ex: 'olvid/daemon/datatypes/v1/message.proto'
	package: str # ex: 'olvid.daemon.datatypes.v1'
	# Items to be rendered in the datatypes section (ignores Requests/Responses)
	items: List[Union[ParsedMessage, ParsedEnum]] = field(default_factory=list)

@dataclass
class ProjectModel:
	"""The root data structure holding the entire parsed Protobuf project."""
	files: Dict[str, ParsedFile] = field(default_factory=dict)
	all_messages: Dict[str, ParsedMessage] = field(default_factory=dict)
	all_enums: Dict[str, ParsedEnum] = field(default_factory=dict)
	commands: Dict[str, ParsedService] = field(default_factory=dict)
	notifications: Dict[str, ParsedService] = field(default_factory=dict)
	admins: Dict[str, ParsedService] = field(default_factory=dict)

	@property
	def datatypes_files(self) -> Dict[str, ParsedFile]:
		return {f: v for f, v in self.files.items() if f.startswith("olvid/daemon/datatypes")}


# --- PARSER ---
class DescriptorParser:
	"""Responsible for reading the FileDescriptorSet and building the ProjectModel."""

	def __init__(self, desc_set: FileDescriptorSet):
		self.desc_set = desc_set
		self.model = ProjectModel()
		self.current_comments: Dict[Tuple[int, ...], str] = {}
		self.current_spans: Dict[Tuple[int, ...], int] = {}

	def parse(self) -> ProjectModel:
		for file_proto in self.desc_set.file:
			self._build_source_info_maps(file_proto)

			filepath: str = file_proto.name
			filename: str = os.path.basename(filepath)
			if filepath not in self.model.files:
				self.model.files[filepath] = ParsedFile(filename=filename, filepath=filepath, package=file_proto.package)
			file: ParsedFile = self.model.files[filepath]

			# Extract Top-level Enums (tag 5)
			self._extract_enums(file_proto, tuple(), 5, "", file, file_proto.package)

			# Extract Top-level Messages (tag 4)
			self._extract_messages(file_proto, tuple(), 4, "", file, file_proto.package)

			# Extract Services (tag 6)
			self._extract_services(file_proto, file)

		# Clean up empty files
		self.model.files = {f: v for f, v in self.model.files.items() if v.items}

		# link field types with associated message or enum
		self._link_field_type_with_parsed_items()
		self._link_rpc_input_and_output_with_message()

		return self.model

	def _build_source_info_maps(self, file_proto: Any) -> None:
		"""Maps Protobuf source code paths to their comments and line numbers."""
		self.current_comments.clear()
		self.current_spans.clear()

		for location in file_proto.source_code_info.location:
			path = tuple(location.path)
			comment = ""

			if location.leading_detached_comments:
				for detached in location.leading_detached_comments:
					comment += detached + "\n"

			if location.leading_comments:
				comment += location.leading_comments + "\n"
			if location.trailing_comments:
				comment += location.trailing_comments + "\n"

			cleaned_lines = [line.strip().lstrip("*").strip() for line in comment.splitlines()]
			final_comment = "\n".join(cleaned_lines).strip()

			if final_comment:
				self.current_comments[path] = final_comment

			if location.span:
				self.current_spans[path] = location.span[0]

	def _get_clean_type_name(self, type_name: str, package: str) -> str:
		"""Removes the package prefix to get the relative message/enum name."""
		prefix = f".{package}." if package else "."
		if type_name.startswith(prefix):
			return type_name[len(prefix):]
		return type_name.split('.')[-1]

	def _extract_enums(self, container: Any, base_path: Tuple[int, ...], tag: int, prefix: str, file: ParsedFile, file_package: str) -> None:
		"""Recursively extracts enums and populates the model."""
		for i, enum_proto in enumerate(container.enum_type):
			enum_path = base_path + (tag, i)
			desc = self.current_comments.get(enum_path, "")
			full_name = f"{prefix}{enum_proto.name}"
			full_type = f"{file_package}.{full_name}"

			parsed_enum = ParsedEnum(
				name=full_name,
				full_type=full_type,
				desc=desc,
				line=self.current_spans.get(enum_path, 0),
				file=file
			)

			for j, enum_val in enumerate(enum_proto.value):
				val_path = enum_path + (2, j)
				val_desc = self.current_comments.get(val_path, "")
				parsed_enum.values[enum_val.name] = ParsedEnumValue(
					name=enum_val.name,
					number=enum_val.number,
					desc=val_desc
				)

			self.model.files[file.filepath].items.append(parsed_enum)
			self.model.all_enums[full_type] = parsed_enum

	def _extract_messages(self, container: Any, base_path: Tuple[int, ...], tag: int, prefix: str, file: ParsedFile, file_package: str) -> None:
		"""Recursively extracts messages, fields, and nested structures."""
		msg_list = container.message_type if hasattr(container, "message_type") else container.nested_type

		for i, msg in enumerate(msg_list):
			message_path = base_path + (tag, i)
			message_desc = self.current_comments.get(message_path, "")
			message_full_name = f"{prefix}{msg.name}"
			message_full_type = f"{file_package}.{message_full_name}"

			# 1. Nested Enums (tag 4)
			self._extract_enums(msg, message_path, 4, f"{message_full_name}.", file, file_package)

			# 2. Nested Messages (tag 3)
			self._extract_messages(msg, message_path, 3, f"{message_full_name}.", file, file_package)

			# 3. Fields & OneOfs
			parsed_msg = ParsedMessage(
				name=message_full_name,
				full_type=message_full_type,
				desc=message_desc,
				line=self.current_spans.get(message_path, 0),
				file=file
			)
			oneof_track: Set[int] = set()

			for j, field in enumerate(msg.field):
				field_path = message_path + (2, j)
				field_desc = self.current_comments.get(field_path, "")

				field_type: str = PROTO_TYPES.get(field.type, "unknown")
				field_full_type: str = field.type_name.removeprefix(".")

				if field.type in (11, 14):  # Message or Enum
					field_type = self._get_clean_type_name(field.type_name, file_package)
					field_is_scalar = False
					field_is_message: bool = field.type == 11
					field_is_enum: bool = field.type == 14
				else:
					field_is_scalar = True
					field_is_message: bool = False
					field_is_enum: bool = False

				# Check for modifiers
				is_repeated: bool = False
				is_optional: bool = False
				is_deprecated: bool = False
				# repeated fields are optional, by design
				if field.label == 3:
					is_repeated = True
				elif getattr(field, "proto3_optional", False):
					is_optional = True
				if getattr(field.options, "deprecated", False):
					is_deprecated = True

				# Handle oneof
				is_real_oneof = field.HasField("oneof_index") and not getattr(field, "proto3_optional", False)

				if is_real_oneof:
					idx = field.oneof_index
					oneof_name = msg.oneof_decl[idx].name

					oneof_sub_field: ParsedField = ParsedField(
						name=field.name,
						desc=field_desc,
						type=field_type,
						full_type=field_full_type,
						is_scalar=field_is_scalar,
						is_repeated=is_repeated,
						is_optional=is_optional,
						is_deprecated=is_deprecated,
						is_message=field_is_message,
						is_enum=field_is_enum,
					)

					if idx not in oneof_track:
						oneof_track.add(idx)
						oneof_path = message_path + (8, idx)
						oneof_desc = self.current_comments.get(oneof_path, "")

						oneof_field = ParsedOneofField(
							is_repeated=is_repeated,
							is_deprecated=is_deprecated,
							name=oneof_name,
							desc=oneof_desc,
							subfields=[oneof_sub_field]
						)
						parsed_msg.fields.append(oneof_field)
					else:
						# Append to existing group block
						for fd in parsed_msg.fields:
							if isinstance(fd, ParsedOneofField) and fd.name == oneof_name:
								fd.subfields.append(oneof_sub_field)
								break
				else:
					parsed_msg.fields.append(ParsedField(
						name=field.name,
						type=field_type,
						full_type=field_full_type,
						is_scalar=field_is_scalar,
						is_repeated=is_repeated,
						is_optional=is_optional,
						is_deprecated=is_deprecated,
						desc=field_desc,
						is_message=field_is_message,
						is_enum=field_is_enum,
					))

			self.model.all_messages[message_full_type] = parsed_msg

			if not message_full_name.endswith("Request") and not message_full_name.endswith("Response"):
				self.model.files[file.filepath].items.append(parsed_msg)

	def _extract_services(self, file_proto: Any, file: ParsedFile) -> None:
		"""Extracts RPC Services and their methods."""
		for i, svc in enumerate(file_proto.service):
			svc_path = (6, i)
			desc = self.current_comments.get(svc_path, "")
			core_datatype = svc.name.replace("CommandService", "").replace("NotificationService", "").replace("AdminService", "")

			parsed_svc = ParsedService(name=svc.name, datatype=core_datatype, desc=desc, file=file)

			for j, method in enumerate(svc.method):
				method_path = (6, i, 2, j)
				method_desc = self.current_comments.get(method_path, "")
				input_clean = method.input_type.removeprefix(".")
				output_clean = method.output_type.removeprefix(".")

				parsed_svc.rpcs[method.name] = ParsedRPC(
					name=method.name,
					desc=method_desc,
					input_name=input_clean,
					output_name=output_clean,
					client_streaming=method.client_streaming,
					server_streaming=method.server_streaming,
				)

			if svc.name.endswith("CommandService"):
				self.model.commands[svc.name] = parsed_svc
			elif svc.name.endswith("NotificationService"):
				self.model.notifications[svc.name] = parsed_svc
			elif svc.name.endswith("AdminService"):
				self.model.admins[svc.name] = parsed_svc

	def _link_field_type_with_parsed_items(self):
		def recursive_link(fd: ParsedField | ParsedOneofField):
			if isinstance(fd, ParsedOneofField):
				for subfd in fd.subfields:
					recursive_link(subfd)
			if isinstance(fd, ParsedField):
				if fd.is_message:
					fd.message = self.model.all_messages.get(fd.full_type)
					if fd.message is None:
						print(f"message not found: {fd.full_type}")
				if fd.is_enum:
					fd.enum = self.model.all_enums.get(fd.full_type)
					if fd.enum is None:
						print(f"enum not found: {fd.type}")

		for message in self.model.all_messages.values():
			for fd in message.fields:
				recursive_link(fd)

	def _link_rpc_input_and_output_with_message(self):
		def recursive_link():
			pass
		for service in [c for c in self.model.commands.values()] + [n for n in self.model.notifications.values()] + [a for a in self.model.admins.values()]:
			for rpc in service.rpcs.values():
				rpc.input = self.model.all_messages.get(rpc.input_name)
				rpc.output = self.model.all_messages.get(rpc.output_name)
				if rpc.input is None :
					print(f"rpc: input not found: {rpc.input_name}")
				if rpc.output is None:
					print(f"rpc: output not found: {rpc.output_name}")

# --- GENERATOR ---
class MarkdownRenderer:
	"""Responsible for converting the parsed ProjectModel into MyST Markdown files."""

	def __init__(self, model: ProjectModel, output_dir: str):
		self.model = model
		self.output_dir = output_dir

	def generate_all(self) -> None:
		os.makedirs(self.output_dir, exist_ok=True)
		self._generate_datatypes()
		self._generate_service_file(self.model.commands, "Commands", "", "commands.md")
		self._generate_service_file(self.model.notifications, "Notifications", "Events you can subscribe to, and notification content.", "notifications.md")
		self._generate_service_file(self.model.admins, "Admin Commands", "Privileged commands requiring a valid admin client key.", "admins.md")

	@staticmethod
	def _get_sort_key(name: str) -> int:
		base = os.path.basename(name).replace('.proto', '').lower()
		for i, pref in enumerate(PREFERRED_FILES):
			if pref.lower() == base:
				return i
		return 999

	@staticmethod
	def _compute_reference_name(entity: ParsedFile | ParsedService | ParsedRPC | ParsedMessage | ParsedEnum):
		if isinstance(entity, ParsedFile):
			return f"file-{entity.filename.removesuffix('.proto').lower()}"
		elif isinstance(entity, ParsedMessage):
			return f"message-{entity.name.lower()}"
		elif isinstance(entity, ParsedService):
			return f"service-{entity.name.lower()}"
		elif isinstance(entity, ParsedRPC):
			return f"rpc-{entity.name.lower()}"
		elif isinstance(entity, ParsedEnum):
			return f"enum-{entity.name.lower()}"
		raise ValueError(f"Unknown entity type: {type(entity)}")

	def _generate_message_field(self, fd: ParsedField|ParsedOneofField) -> list[str]:
		lines: list[str] = []
		if isinstance(fd, ParsedOneofField):
			desc_str = f" - *{fd.desc}*" if fd.desc else ""
			lines.append(f"* **Oneof `{fd.name}`**{desc_str}:")
			for oneof_subfield in fd.subfields:
				# add manual indentation
				lines.extend(["  " + sbf for sbf in self._generate_message_field(oneof_subfield)])
		elif isinstance(fd, ParsedField):
			modifiers = []
			print_type: str = fd.type
			# if this field is a message / an enum replace by appropriate link
			if fd.is_message:
				print_type = f"{{ref}}`{self._compute_reference_name(fd.message)}`"
			elif fd.is_enum:
				print_type = f"{{ref}}`{self._compute_reference_name(fd.enum)}`"
			# add modifiers before type
			if fd.is_repeated:
				modifiers.append("**repeated**")
			elif fd.is_optional:
				modifiers.append("**optional**")
			if fd.is_deprecated:
				modifiers.append("***deprecated***")
			if modifiers:
				print_type = f"{', '.join(modifiers)} " + print_type
			# add description after type
			if fd.desc:
				print_type += f" - *{fd.desc}*"
			lines.append(f"* `{fd.name}` ({print_type})")
		return lines

	def _generate_message(self, item: ParsedMessage|ParsedEnum, depth: int = 0) -> list[str]:
		lines: list[str] = []
		h_level = "#" * min(6, 3 + depth)
		fence = ":" * (7 - depth)

		# manage the card only if depth is not zero, this means you are in a nested message
		if depth > 0:
			lines.append(f"{fence}{{card}}")
			lines.append(f"({self._compute_reference_name(item)})=")
			lines.append(f"{h_level} {item.name}\n")

		if item.desc:
			lines.append(f"> {item.desc.replace('\n', '  \n> ')}\n")

		if isinstance(item, ParsedMessage):
			if item.fields:
				lines.append("**Fields:**")
				for fd in item.fields:
					lines.extend(self._generate_message_field(fd))
			else:
				lines.append("*No fields.*")

		elif isinstance(item, ParsedEnum):
			lines.append("**Enum Values:**")
			sorted_enum_vals = sorted(item.values.items(), key=lambda x: x[1].number)
			for val_name, enum_val in sorted_enum_vals:
				line = f"* `{val_name}`: {enum_val.number}"
				if enum_val.desc:
					line += f" - *{enum_val.desc}*"
				lines.append(line)

		if depth > 0:
			lines.append(f"{fence}")

		return lines

	def _generate_datatypes(self) -> None:
		dt_lines: List[str] = [
			"# Datatypes\n",
			"This section describes the core entities used by Olvid daemon and exposed entrypoints.  ",
		]
		dt_lines.extend([":::{contents} Datatypes", ":depth: 1", ":local:", ":::", ""])

		sorted_files: list[ParsedFile] = sorted(self.model.datatypes_files.values(), key=lambda file: (self._get_sort_key(file.filepath), file))

		for file in sorted_files:
			sorted_items = sorted(file.items, key=lambda x: x.line)

			base_name = os.path.basename(file.filepath).replace('.proto', '').lower()
			file_msgs_lower = [item.name.lower() for item in sorted_items if item.type == "message"]

			dt_lines.append(f"({self._compute_reference_name(file)})=")
			dt_lines.append(f"## {os.path.basename(file.filepath).removesuffix('.proto').title()}\n")

			# Link relevant endpoints
			file_cmds, file_notifs, file_admins = [], [], []
			for cmd, service in self.model.commands.items():
				if service.datatype.lower() == base_name or service.datatype.lower() in file_msgs_lower:
					file_cmds.append(service)
			for notif, service in self.model.notifications.items():
				if service.datatype.lower() == base_name or service.datatype.lower() in file_msgs_lower:
					file_notifs.append(service)
			for admin, service in self.model.admins.items():
				if service.datatype.lower() == base_name or service.datatype.lower() in file_msgs_lower:
					file_admins.append(service)

			if file_cmds or file_notifs or file_admins:
				dt_lines.append("> **Related Endpoints:**")
				for cmd in file_cmds:
					dt_lines.append(f"> * **Command:** {{ref}}`{self._compute_reference_name(cmd)}`")
				for notif in file_notifs:
					dt_lines.append(f"> * **Notification:** {{ref}}`{self._compute_reference_name(notif)}`")
				for admin in file_admins:
					dt_lines.append(f"> * **Admin:** {{ref}}`{self._compute_reference_name(admin)}`")
				dt_lines.append("\n")

			active_path = []
			open_fences = []

			for item in sorted_items:
				parts = item.name.split('.')
				parent_parts = parts[:-1]

				# Close cards that are no longer active in the current hierarchy
				while active_path and parent_parts[:len(active_path)] != active_path:
					dt_lines.append(open_fences.pop())
					active_path.pop()

				depth = len(parts) - 1
				fence = ":" * (7 - depth)
				h_level = "#" * min(6, 3 + depth)

				if depth == 0:
					dt_lines.append(f"({self._compute_reference_name(item)})=")
					dt_lines.append(f"{h_level} {item.name}\n")
					dt_lines.append(f"{fence}{{card}}")

				dt_lines.extend(self._generate_message(item, depth))

				dt_lines.append("")  # padding inside the card

				if depth == 0:
					open_fences.append(fence)
					active_path.append(parts[-1])

			while open_fences:
				dt_lines.append(open_fences.pop())

			dt_lines.append("\n---\n")

		if dt_lines[-1] == "\n---\n":
			dt_lines.pop(-1)

		with open(os.path.join(self.output_dir, "datatypes.md"), "w", encoding="utf-8") as f:
			f.write("\n".join(dt_lines))

	def _build_rpc_input_or_output(self, message: ParsedMessage, label: str, is_stream: bool, skip_desc: bool = False) -> List[str]:
		stream_tag = " *(Stream)*" if is_stream else ""
		lines = [
			f"({self._compute_reference_name(message)})=",
			f"**{label}{stream_tag}**: *{message.name}*"
		]

		if message.desc and not skip_desc:
			lines.append(f"{message.desc}\n")

		if message.fields:
			for fd in message.fields:
				lines.extend(self._generate_message_field(fd))
		else:
			lines.append("* *Empty payload.*")

		lines.append("")
		return lines

	def _generate_service_file(self, service_dict: Dict[str, ParsedService], title: str, subtitle: str, output_filename: str) -> None:
		lines: List[str] = [f"# {title}\n\n{subtitle}\n"]
		lines.extend([f":::{{contents}} {title}", ":depth: 1", ":local:", ":::"])

		sorted_services: list[ParsedService] = sorted(service_dict.values(), key=lambda serv: (self._get_sort_key(serv.datatype), serv))

		for service in sorted_services:

			lines.append(f"({self._compute_reference_name(service)})=")
			lines.append(f"## {re.sub(r'(\w)([A-Z])', r'\1 \2', service.name)}\n")

			lines.append(f":::{{admonition}} Info")
			lines.append(service.desc.removeprefix(service.datatype).strip().replace("\n", "  \n"))
			if len(service.desc.strip().lower().removeprefix(service.datatype.lower()).strip()) > 0:
				lines.append("\n")

			# manually compute link to associated datatype file
			reference: str = f"file-{service.datatype.lower()}"
			# an hardcoded set of links to override because they do not exist in reality
			reference_aliases: dict[str, str] = {
				"file-clientkey": "file-identity", "file-discussionstorage": "file-storage", "file-tool": None
			}
			if reference in reference_aliases.keys():
				reference: str = reference_aliases[reference]
			if reference is not None:
				lines.append(f"**Associated Datatype:** {{ref}}`{reference}`")
			lines.append(":::")

			for rpc in service.rpcs.values():
				rpc_desc = rpc.desc
				req_msg = rpc.input

				# Hoisting Logic: if no RPC comment, borrow from Request message
				hoisted_req_desc = False
				if not rpc_desc and req_msg and req_msg.desc:
					rpc_desc = req_msg.desc
					hoisted_req_desc = True

				lines.append(f"({self._compute_reference_name(rpc)})=")
				lines.append(f"### {rpc.name}")
				lines.append(f"::::::{{card}}")

				# parse description: remove rpc name from comment, and extract error codes
				rpc_desc = rpc_desc.strip().removeprefix(rpc.name).strip()
				rpc_desc_comment: str = rpc_desc.split("**Error codes**:")[0].strip()
				rpc_desc_error_codes: str = rpc_desc.split("**Error codes**:")[1].strip() if "**Error codes**:" in rpc_desc else ""
				if rpc_desc_comment:
					lines.append(f"> {rpc_desc_comment.replace('\n', '  \n> ')}\n")

				# print request and response details
				req_label = "Request" if "Notification" not in title else "Subscription"
				resp_label = "Response" if "Notification" not in title else "Notification"
				lines.extend(self._build_rpc_input_or_output(rpc.input, req_label, rpc.client_streaming, skip_desc=hoisted_req_desc))
				lines.extend(self._build_rpc_input_or_output(rpc.output, resp_label, rpc.server_streaming))

				# manually print add messages declared with this rpc, that are not input or output
				associated_messages: list[ParsedMessage] = [m for m in project_model.all_messages.values() if m.name.startswith(rpc.input.name) and m.name != rpc.input.name]
				associated_messages.extend([m for m in project_model.all_messages.values() if m.name.startswith(rpc.output.name) and m.name != rpc.output.name])
				if associated_messages:
					associated_messages = sorted(associated_messages, key=lambda m: len(m.name))
					for m in associated_messages:
						lines.extend(self._generate_message(m, depth=2))

				# print error codes
				if rpc_desc_error_codes:
					lines.extend([
						"**Error Codes**:",
						"- " + rpc_desc_error_codes.replace("\n", "\n - ")
					])
				lines.append(f"::::::\n")

			lines.append("---\n")

		# Strip trailing separator
		if lines[-1] == "---\n":
			lines.pop(-1)

		with open(os.path.join(self.output_dir, output_filename), "w", encoding="utf-8") as f:
			f.write("\n".join(lines))


# --- MAIN ---
if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("specify descriptor file to use")
		exit(1)
	if len(sys.argv) == 2:
		print("specify output directory")
		exit(1)

	descriptor_file = sys.argv[1]
	output_dir = sys.argv[2]
	if not os.path.exists(descriptor_file):
		print(f"Error: '{descriptor_file}' not found. Run `buf build -o {descriptor_file}` first.")
		sys.exit(1)

	# 1. Parse FileDescriptorSet into internal object model
	with open(descriptor_file, "rb") as f:
		desc_set = FileDescriptorSet()
		desc_set.ParseFromString(f.read())

	parser = DescriptorParser(desc_set)
	project_model = parser.parse()

	# 2. Render Markdown from the structured object model
	renderer = MarkdownRenderer(project_model, output_dir)
	renderer.generate_all()

	print("generate_references.py: Success")
