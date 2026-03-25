import os
import re
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Any, Set, Union
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
	desc: str
	line: int
	values: Dict[str, ParsedEnumValue] = field(default_factory=dict)

	@property
	def type(self) -> str:
		return "enum"

@dataclass
class ParsedField:
	name: str
	f_type: str = ""
	is_oneof: bool = False
	desc: str = ""
	sub_fields: List[Tuple[str, str]] = field(default_factory=list)

@dataclass
class ParsedMessage:
	name: str
	desc: str
	line: int
	fields: List[ParsedField] = field(default_factory=list)

	@property
	def type(self) -> str:
		return "message"

@dataclass
class ParsedRPC:
	name: str
	desc: str
	input: str
	output: str
	client_streaming: bool
	server_streaming: bool

@dataclass
class ParsedService:
	name: str
	datatype: str
	desc: str
	rpcs: Dict[str, ParsedRPC] = field(default_factory=dict)

@dataclass
class ParsedFile:
	filename: str
	package: str
	# Items to be rendered in the datatypes section (ignores Requests/Responses)
	items: List[Union[ParsedMessage, ParsedEnum]] = field(default_factory=list)

@dataclass
class ProjectModel:
	"""The root data structure holding the entire parsed Protobuf project."""
	files: Dict[str, ParsedFile] = field(default_factory=dict)
	all_messages: Dict[str, ParsedMessage] = field(default_factory=dict)
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

			filename = file_proto.name
			if filename not in self.model.files:
				self.model.files[filename] = ParsedFile(filename=filename, package=file_proto.package)

			# Extract Top-level Enums (tag 5)
			self._extract_enums(file_proto, tuple(), 5, "", filename)

			# Extract Top-level Messages (tag 4)
			self._extract_messages(file_proto, tuple(), 4, "", filename, file_proto.package)

			# Extract Services (tag 6)
			self._extract_services(file_proto)

		# Clean up empty files
		self.model.files = {f: v for f, v in self.model.files.items() if v.items}
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

	def _extract_enums(self, container: Any, base_path: Tuple[int, ...], tag: int, prefix: str, filename: str) -> None:
		"""Recursively extracts enums and populates the model."""
		for i, enum_proto in enumerate(container.enum_type):
			enum_path = base_path + (tag, i)
			desc = self.current_comments.get(enum_path, "")
			full_name = f"{prefix}{enum_proto.name}"

			parsed_enum = ParsedEnum(
				name=full_name,
				desc=desc,
				line=self.current_spans.get(enum_path, 0)
			)

			for j, enum_val in enumerate(enum_proto.value):
				val_path = enum_path + (2, j)
				val_desc = self.current_comments.get(val_path, "")
				parsed_enum.values[enum_val.name] = ParsedEnumValue(
					name=enum_val.name,
					number=enum_val.number,
					desc=val_desc
				)

			self.model.files[filename].items.append(parsed_enum)

	def _extract_messages(self, container: Any, base_path: Tuple[int, ...], tag: int, prefix: str, filename: str, file_package: str) -> None:
		"""Recursively extracts messages, fields, and nested structures."""
		msg_list = container.message_type if hasattr(container, "message_type") else container.nested_type

		for i, msg in enumerate(msg_list):
			msg_path = base_path + (tag, i)
			desc = self.current_comments.get(msg_path, "")
			full_name = f"{prefix}{msg.name}"

			# 1. Nested Enums (tag 4)
			self._extract_enums(msg, msg_path, 4, f"{full_name}.", filename)

			# 2. Nested Messages (tag 3)
			self._extract_messages(msg, msg_path, 3, f"{full_name}.", filename, file_package)

			# 3. Fields & OneOfs
			parsed_msg = ParsedMessage(
				name=full_name,
				desc=desc,
				line=self.current_spans.get(msg_path, 0)
			)
			oneof_track: Set[int] = set()

			for j, field in enumerate(msg.field):
				field_path = msg_path + (2, j)
				field_desc = self.current_comments.get(field_path, "")

				f_type = PROTO_TYPES.get(field.type, "unknown")
				if field.type in (11, 14):  # Message or Enum
					if field.type_name.startswith(".google.protobuf."):
						f_type = f"`{field.type_name.split('.')[-1]}`"
					else:
						clean_type = self._get_clean_type_name(field.type_name, file_package)
						f_type = f"{{ref}}`datatype-{clean_type.lower()}`"

				# Check for modifiers
				modifiers = []
				if field.label == 3:  # LABEL_REPEATED
					f_type = f"**repeated** {f_type}"
				elif getattr(field, "proto3_optional", False):
					f_type = f"**optional** {f_type}"

				if getattr(field.options, "deprecated", False):
					f_type = f"***deprecated*** {f_type}"

				if modifiers:
					f_type = f" **{', '.join(modifiers)}** " + f_type

				if field_desc:
					f_type += f" - *{field_desc}*"

				# Handle oneof
				is_real_oneof = field.HasField("oneof_index") and not getattr(field, "proto3_optional", False)

				if is_real_oneof:
					idx = field.oneof_index
					oneof_name = msg.oneof_decl[idx].name

					if idx not in oneof_track:
						oneof_track.add(idx)
						oneof_path = msg_path + (8, idx)
						oneof_desc = self.current_comments.get(oneof_path, "")

						oneof_field = ParsedField(
							is_oneof=True,
							name=oneof_name,
							desc=oneof_desc
						)
						oneof_field.sub_fields.append((field.name, f_type))
						parsed_msg.fields.append(oneof_field)
					else:
						# Append to existing group block
						for fd in parsed_msg.fields:
							if fd.is_oneof and fd.name == oneof_name:
								fd.sub_fields.append((field.name, f_type))
								break
				else:
					parsed_msg.fields.append(ParsedField(
						is_oneof=False,
						name=field.name,
						f_type=f_type
					))

			self.model.all_messages[full_name] = parsed_msg

			if not full_name.endswith("Request") and not full_name.endswith("Response"):
				self.model.files[filename].items.append(parsed_msg)

	def _extract_services(self, file_proto: Any) -> None:
		"""Extracts RPC Services and their methods."""
		for i, svc in enumerate(file_proto.service):
			svc_path = (6, i)
			desc = self.current_comments.get(svc_path, "")
			core_datatype = svc.name.replace("CommandService", "").replace("NotificationService", "").replace("AdminService", "")

			parsed_svc = ParsedService(name=svc.name, datatype=core_datatype, desc=desc)

			for j, method in enumerate(svc.method):
				method_path = (6, i, 2, j)
				method_desc = self.current_comments.get(method_path, "")
				input_clean = self._get_clean_type_name(method.input_type, file_proto.package)
				output_clean = self._get_clean_type_name(method.output_type, file_proto.package)

				parsed_svc.rpcs[method.name] = ParsedRPC(
					name=method.name,
					desc=method_desc,
					input=input_clean,
					output=output_clean,
					client_streaming=method.client_streaming,
					server_streaming=method.server_streaming
				)

			if svc.name.endswith("CommandService"):
				self.model.commands[svc.name] = parsed_svc
			elif svc.name.endswith("NotificationService"):
				self.model.notifications[svc.name] = parsed_svc
			elif svc.name.endswith("AdminService"):
				self.model.admins[svc.name] = parsed_svc


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

	def _generate_datatypes(self) -> None:
		dt_lines: List[str] = [
			"# Datatypes\n",
			"This section describes the core entities used by Olvid daemon and exposed entrypoints.  ",
		]
		dt_lines.extend([":::{contents} Datatypes", ":depth: 1", ":local:", ":::", ""])

		sorted_files = sorted(self.model.datatypes_files.keys(), key=lambda f: (self._get_sort_key(f), f))

		for filename in sorted_files:
			file_info = self.model.files[filename]
			sorted_items = sorted(file_info.items, key=lambda x: x.line)

			base_name = os.path.basename(filename).replace('.proto', '').lower()
			file_msgs_lower = [item.name.lower() for item in sorted_items if item.type == "message"]

			dt_lines.append(f"(datatype-{base_name.lower()})=")
			dt_lines.append(f"## {os.path.basename(filename).removesuffix('.proto').title()}\n")

			# Link relevant endpoints
			file_cmds, file_notifs, file_admins = [], [], []
			for cmd, info in self.model.commands.items():
				if info.datatype.lower() == base_name or info.datatype.lower() in file_msgs_lower:
					file_cmds.append(cmd)
			for notif, info in self.model.notifications.items():
				if info.datatype.lower() == base_name or info.datatype.lower() in file_msgs_lower:
					file_notifs.append(notif)
			for admin, info in self.model.admins.items():
				if info.datatype.lower() == base_name or info.datatype.lower() in file_msgs_lower:
					file_admins.append(admin)

			if file_cmds or file_notifs or file_admins:
				dt_lines.append("> **Related Endpoints:**")
				for cmd in file_cmds:
					dt_lines.append(f"> * **Command:** {{ref}}`service-{cmd.lower()}`")
				for notif in file_notifs:
					dt_lines.append(f"> * **Notification:** {{ref}}`service-{notif.lower()}`")
				for admin in file_admins:
					dt_lines.append(f"> * **Admin:** {{ref}}`service-{admin.lower()}`")
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
				h_level = "#" * min(6, 3 + depth)
				fence = ":" * (7 - depth)

				if depth == 0:
					if item.name.lower() != base_name:
						dt_lines.append(f"(datatype-{item.name.lower()})=")
					dt_lines.append(f"{h_level} {item.name}\n")
					dt_lines.append(f"{fence}{{card}}")
				else:
					dt_lines.append(f"{fence}{{card}}")
					if item.name.lower() != base_name:
						dt_lines.append(f"(datatype-{item.name.lower()})=")
					dt_lines.append(f"{h_level} {item.name}\n")

				open_fences.append(fence)
				active_path.append(parts[-1])

				if item.desc:
					dt_lines.append(f"> {item.desc.replace('\n', '  \n> ')}\n")

				if isinstance(item, ParsedMessage):
					if item.fields:
						dt_lines.append("**Fields:**")
						for fd in item.fields:
							if fd.is_oneof:
								desc_str = f" - *{fd.desc}*" if fd.desc else ""
								dt_lines.append(f"* **Oneof `{fd.name}`**{desc_str}:")
								for o_name, o_type in fd.sub_fields:
									dt_lines.append(f"  * `{o_name}` ({o_type})")
							else:
								dt_lines.append(f"* `{fd.name}` ({fd.f_type})")
					else:
						dt_lines.append("*No fields.*")

				elif isinstance(item, ParsedEnum):
					dt_lines.append("**Enum Values:**")
					sorted_enum_vals = sorted(item.values.items(), key=lambda x: x[1].number)
					for val_name, enum_val in sorted_enum_vals:
						line = f"* `{val_name}`: {enum_val.number}"
						if enum_val.desc:
							line += f" - *{enum_val.desc}*"
						dt_lines.append(line)

				dt_lines.append("")  # padding inside the card

			while open_fences:
				dt_lines.append(open_fences.pop())

			dt_lines.append("\n---\n")

		if dt_lines[-1] == "\n---\n":
			dt_lines.pop(-1)

		with open(os.path.join(self.output_dir, "datatypes.md"), "w", encoding="utf-8") as f:
			f.write("\n".join(dt_lines))

	def _build_payload_block(self, msg_name: str, label: str, is_stream: bool, skip_desc: bool = False) -> List[str]:
		stream_tag = " *(Stream)*" if is_stream else ""
		lines = [f"**{label}{stream_tag}**: *{msg_name}*"]

		msg_details = self.model.all_messages.get(msg_name)
		if msg_details:
			if msg_details.desc and not skip_desc:
				lines.append(f"{msg_details.desc}\n")

			if msg_details.fields:
				for fd in msg_details.fields:
					if fd.is_oneof:
						desc_str = f" - *{fd.desc}*" if fd.desc else ""
						lines.append(f"* **Oneof `{fd.name}`**{desc_str}:")
						for o_name, o_type in fd.sub_fields:
							lines.append(f"  * `{o_name}` ({o_type})")
					else:
						lines.append(f"* `{fd.name}` ({fd.f_type})")
			else:
				lines.append("* *Empty payload.*")
		else:
			lines.append("* *Empty payload.*")

		lines.append("")
		return lines

	def _generate_service_file(self, service_dict: Dict[str, ParsedService], title: str, subtitle: str, output_filename: str) -> None:
		lines: List[str] = [f"# {title}\n\n{subtitle}\n"]
		lines.extend([f":::{{contents}} {title}", ":depth: 1", ":local:", ":::"])

		sorted_services = sorted(service_dict.keys(), key=lambda k: (self._get_sort_key(service_dict[k].datatype), k))

		for name in sorted_services:
			details = service_dict[name]

			lines.append(f"(service-{name.lower()})=")
			lines.append(f"## {re.sub(r'(\w)([A-Z])', r'\1 \2', name)}\n")

			lines.append(f":::{{admonition}} Info")
			lines.append(details.desc.removeprefix(details.datatype).strip().replace("\n", "  \n"))
			if len(details.desc.strip().lower().removeprefix(details.datatype.lower()).strip()) > 0:
				lines.append("\n")
			lines.append(f"**Associated Datatype:** {{ref}}`datatype-{details.datatype.lower()}`")
			lines.append(":::")

			for rpc_name, rpc_info in details.rpcs.items():
				rpc_desc = rpc_info.desc
				req_msg = self.model.all_messages.get(rpc_info.input)

				# Hoisting Logic: if no RPC comment, borrow from Request message
				hoisted_req_desc = False
				if not rpc_desc and req_msg and req_msg.desc:
					rpc_desc = req_msg.desc
					hoisted_req_desc = True

				lines.append(f"### {rpc_name}")
				lines.append(f":::{{card}}")

				# parse description: remove rpc name from comment, and extract error codes
				rpc_desc = rpc_desc.strip().removeprefix(rpc_name).strip()
				rpc_desc_comment: str = rpc_desc.split("**Error codes**:")[0].strip()
				rpc_desc_error_codes: str = rpc_desc.split("**Error codes**:")[1].strip() if "**Error codes**:" in rpc_desc else ""
				if rpc_desc_comment:
					lines.append(f"> {rpc_desc_comment.replace('\n', '  \n> ')}\n")

				req_label = "Request" if "Notification" not in title else "Subscription"
				resp_label = "Response" if "Notification" not in title else "Notification"

				lines.extend(self._build_payload_block(rpc_info.input, req_label, rpc_info.client_streaming, skip_desc=hoisted_req_desc))
				lines.extend(self._build_payload_block(rpc_info.output, resp_label, rpc_info.server_streaming))
				if rpc_desc_error_codes:
					lines.extend([
						"**Error Codes**:",
						"- " + rpc_desc_error_codes.replace("\n", "\n - ")
					])
				lines.append(f":::\n")

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
