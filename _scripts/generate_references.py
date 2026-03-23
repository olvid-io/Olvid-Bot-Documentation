import os
import sys
from typing import Dict, List, Tuple, Any
from google.protobuf.descriptor_pb2 import FileDescriptorSet

# --- CONFIGURATION ---
PREFERRED_FILES: List[str] = [
	"message", "attachment", "discussion", "contact", "group",
	"identity", "client_key", "invitation", "settings", "storage",
	"keycloak", "call", "backup"
]

# Map protobuf internal type integers to human-readable strings
PROTO_TYPES: Dict[int, str] = {
	1: "double", 2: "float", 3: "int64", 4: "uint64", 5: "int32",
	6: "fixed64", 7: "fixed32", 8: "bool", 9: "string", 11: "message",
	12: "bytes", 13: "uint32", 14: "enum", 15: "sfixed32",
	16: "sfixed64", 17: "sint32", 18: "sint64"
}

def build_source_info_maps(file_proto: Any) -> Tuple[Dict[Tuple[int, ...], str], Dict[Tuple[int, ...], int]]:
	"""Maps Protobuf source code paths to their comments and line numbers."""
	comments_map: Dict[Tuple[int, ...], str] = {}
	span_map: Dict[Tuple[int, ...], int] = {}

	for location in file_proto.source_code_info.location:
		path = tuple(location.path)
		comment = ""

		# Capture detached block comments (e.g., /* ** BackupKeyGet */)
		if location.leading_detached_comments:
			for detached in location.leading_detached_comments:
				comment += detached + "\n"

		if location.leading_comments:
			comment += location.leading_comments + "\n"
		if location.trailing_comments:
			comment += location.trailing_comments + "\n"

		# Clean up block comment prefixes (e.g. `** `) so they don't break Markdown bolding
		cleaned_lines = []
		for line in comment.splitlines():
			line = line.strip().lstrip("*").strip()
			cleaned_lines.append(line)

		final_comment = "\n".join(cleaned_lines).strip()

		if final_comment:
			comments_map[path] = final_comment

		if location.span:
			span_map[path] = location.span[0] # Capture the starting line number

	return comments_map, span_map

def get_clean_type_name(type_name: str, package: str) -> str:
	"""Removes the package prefix to get the relative message/enum name."""
	prefix = f".{package}." if package else "."
	if type_name.startswith(prefix):
		return type_name[len(prefix):]
	return type_name.split('.')[-1]

def extract_enums(container: Any, base_path: Tuple[int, ...], tag: int, prefix: str, filename: str, comments: Dict, spans: Dict, data: Dict) -> None:
	"""Recursively extracts enums."""
	for i, enum_proto in enumerate(container.enum_type):
		enum_path = base_path + (tag, i)
		desc = comments.get(enum_path, "")
		full_name = f"{prefix}{enum_proto.name}"

		values: Dict[str, Tuple[int, str]] = {}
		for j, enum_val in enumerate(enum_proto.value):
			val_path = enum_path + (2, j)
			val_desc = comments.get(val_path, "")
			values[enum_val.name] = (enum_val.number, val_desc)

		item = {
			"type": "enum",
			"name": full_name,
			"desc": desc,
			"values": values,
			"line": spans.get(enum_path, 0)
		}
		data["files"][filename]["items"].append(item)

def extract_messages(container: Any, base_path: Tuple[int, ...], tag: int, prefix: str, filename: str, file_package: str, comments: Dict, spans: Dict, data: Dict) -> None:
	"""Recursively extracts messages, fields, and nested structures."""
	msg_list = container.message_type if hasattr(container, "message_type") else container.nested_type

	for i, msg in enumerate(msg_list):
		msg_path = base_path + (tag, i)
		desc = comments.get(msg_path, "")
		full_name = f"{prefix}{msg.name}"

		# 1. Extract Nested Enums (tag 4 inside messages)
		extract_enums(msg, msg_path, 4, f"{full_name}.", filename, comments, spans, data)

		# 2. Extract Nested Messages (tag 3 inside messages)
		extract_messages(msg, msg_path, 3, f"{full_name}.", filename, file_package, comments, spans, data)

		# 3. Extract Fields and OneOfs
		fields_data = []
		oneof_track = set()

		for j, field in enumerate(msg.field):
			field_path = msg_path + (2, j)
			field_desc = comments.get(field_path, "")

			f_type = PROTO_TYPES.get(field.type, "unknown")
			if field.type in (11, 14): # Message or Enum
				if field.type_name.startswith(".google.protobuf."):
					f_type = f"`{field.type_name.split('.')[-1]}`"
				else:
					clean_type = get_clean_type_name(field.type_name, file_package)
					f_type = f"{{ref}}`datatype-{clean_type.lower()}`"

			# Check for modifiers (repeated, optional, deprecated)
			modifiers = []
			if field.label == 3: # LABEL_REPEATED
				f_type = f"**repeated** {f_type}"
			elif getattr(field, "proto3_optional", False):
				f_type = f"**optional** {f_type}"

			if getattr(field.options, "deprecated", False):
				f_type = f"***deprecated*** {f_type}"

			if modifiers:
				f_type = f" **{', '.join(modifiers)}** " + f_type

			if field_desc:
				f_type += f" - *{field_desc}*"

			# Handle `oneof` (filter out synthetic proto3 optional oneofs)
			is_real_oneof = field.HasField("oneof_index") and not getattr(field, "proto3_optional", False)

			if is_real_oneof:
				idx = field.oneof_index
				oneof_name = msg.oneof_decl[idx].name

				# If it's the first time seeing this oneof_index, create a group block
				if idx not in oneof_track:
					oneof_track.add(idx)

					# Fetch the block comment associated with the oneof declaration itself
					# The 'oneof_decl' property is located at tag 8 inside a message
					oneof_path = msg_path + (8, idx)
					oneof_desc = comments.get(oneof_path, "")

					fields_data.append({
						"is_oneof": True,
						"name": oneof_name,
						"desc": oneof_desc,
						"sub_fields": [(field.name, f_type)]
					})
				# If group block exists, append to it
				else:
					for fd in fields_data:
						if fd.get("is_oneof") and fd["name"] == oneof_name:
							fd["sub_fields"].append((field.name, f_type))
							break
			else:
				# Standard field handling
				fields_data.append({
					"is_oneof": False,
					"name": field.name,
					"f_type": f_type
				})

		item = {
			"type": "message",
			"name": full_name,
			"desc": desc,
			"fields": fields_data,
			"line": spans.get(msg_path, 0)
		}

		data["all_messages"][full_name] = item

		if not full_name.endswith("Request") and not full_name.endswith("Response"):
			data["files"][filename]["items"].append(item)

def parse_descriptor_set(descriptor_path: str) -> Dict[str, Any]:
	"""Parses the buf-generated descriptor set and structures the data."""
	with open(descriptor_path, "rb") as f:
		desc_set = FileDescriptorSet()
		desc_set.ParseFromString(f.read())

	data: Dict[str, Any] = {
		"files": {},
		"datatypes_files": {},
		"commands": {},
		"notifications": {},
		"admins": {},
		"all_messages": {}
	}

	for file_proto in desc_set.file:
		comments, spans = build_source_info_maps(file_proto)
		filename: str = file_proto.name
		file_package: str = file_proto.package

		if filename not in data["files"]:
			data["files"][filename] = {"items": []}

		# Extract Top-level Enums (tag 5)
		extract_enums(file_proto, tuple(), 5, "", filename, comments, spans, data)

		# Extract Top-level Messages (tag 4)
		extract_messages(file_proto, tuple(), 4, "", filename, file_package, comments, spans, data)

		# Extract Services (tag 6)
		for i, svc in enumerate(file_proto.service):
			svc_path = (6, i)
			desc = comments.get(svc_path, "")
			core_datatype = svc.name.replace("CommandService", "").replace("NotificationService", "").replace("AdminService", "")

			rpcs: Dict[str, Dict[str, Any]] = {}
			for j, method in enumerate(svc.method):
				method_path = (6, i, 2, j)
				method_desc = comments.get(method_path, "")

				input_clean = get_clean_type_name(method.input_type, file_package)
				output_clean = get_clean_type_name(method.output_type, file_package)

				rpcs[method.name] = {
					"desc": method_desc,
					"input": input_clean,
					"client_streaming": method.client_streaming,
					"output": output_clean,
					"server_streaming": method.server_streaming
				}

			svc_info = {"datatype": core_datatype, "desc": desc, "rpcs": rpcs}

			if svc.name.endswith("CommandService"):
				data["commands"][svc.name] = svc_info
			elif svc.name.endswith("NotificationService"):
				data["notifications"][svc.name] = svc_info
			elif svc.name.endswith("AdminService"):
				data["admins"][svc.name] = svc_info

	# Clean up empty files
	data["files"] = {f: v for f, v in data["files"].items() if v["items"]}
	data["datatypes_files"] = {f: v for f, v in data["files"].items() if f.startswith("olvid/daemon/datatypes")}

	return data


def generate_markdown(data: Dict[str, Any], output_dir: str) -> None:
	"""Generates the MyST markdown files from the structured data."""
	os.makedirs(output_dir, exist_ok=True)

	def get_sort_key(name: str) -> int:
		base = os.path.basename(name).replace('.proto', '').lower()
		for i, pref in enumerate(PREFERRED_FILES):
			if pref.lower() in base:
				return i
		return 999

	sorted_datatypes_files = sorted(data["datatypes_files"].keys(), key=lambda f: (get_sort_key(f), f))

	######################
	# --- 1. Datatypes ---
	dt_lines: List[str] = [
		"# 📚️ References\n"
		"This section describes the core entities used by Olvid daemon and exposed entrypoints.  ",
		"This page describe all datatypes used by daemon api, and you can find these api description in the [](commands), [](notifications) and [](admins) sections.\n",
	]
	dt_lines.extend([":::{toctree}", ":maxdepth: 1", ":hidden:", "Datatypes<self>", "commands", "notifications", "admins", ":::", ""])
	dt_lines.extend([":::{contents} Datatypes", ":depth: 1", ":local:", ":::", ""])

	for filename in sorted_datatypes_files:
		file_info = data["files"][filename]

		# Sort all items (enums and messages) by their starting line number in the .proto file
		sorted_items = sorted(file_info.get("items", []), key=lambda x: x["line"])

		base_name = os.path.basename(filename).replace('.proto', '').lower()
		file_msgs_lower = [item["name"].lower() for item in sorted_items if item["type"] == "message"]

		dt_lines.append(f"(datatype-{base_name.lower()})=")
		dt_lines.append(f"## {os.path.basename(filename).removesuffix('.proto').title()}\n")

		file_cmds: List[str] = []
		file_notifs: List[str] = []
		file_admins: List[str] = []

		for cmd, info in data["commands"].items():
			if info["datatype"].lower() == base_name or info["datatype"].lower() in file_msgs_lower:
				file_cmds.append(cmd)
		for notif, info in data["notifications"].items():
			if info["datatype"].lower() == base_name or info["datatype"].lower() in file_msgs_lower:
				file_notifs.append(notif)
		for admin, info in data["admins"].items():
			if info["datatype"].lower() == base_name or info["datatype"].lower() in file_msgs_lower:
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
			parts = item['name'].split('.')
			parent_parts = parts[:-1]

			# Close cards that are no longer active in the current hierarchy
			while active_path and parent_parts[:len(active_path)] != active_path:
				dt_lines.append(open_fences.pop())
				active_path.pop()

			# Dynamic Header Level (H3, H4, etc. based on depth)
			depth = len(parts) - 1
			h_level = "#" * min(6, 3 + depth)

			# Dynamic Fence generation (Outer cards get 7 colons, inner get 6, 5, etc.)
			fence = ":" * (7 - depth)
			# parent card: normal title
			if depth == 0:
				# Set Anchor
				if item['name'].lower() != base_name:
					dt_lines.append(f"(datatype-{item['name'].lower()})=")
				dt_lines.append(f"{h_level} {item['name']}\n")
				dt_lines.append(f"{fence}{{card}}")
			# nested card: title is in card title
			else:
				dt_lines.append(f"{fence}{{card}}")
				# Set Anchor
				if item['name'].lower() != base_name:
					dt_lines.append(f"(datatype-{item['name'].lower()})=")
				dt_lines.append(f"{h_level} {item['name']}\n")

			# Push to stack
			open_fences.append(fence)
			active_path.append(parts[-1])

			if item["desc"]:
				dt_lines.append(f"> {item['desc'].replace('\n', '  \n> ')}\n")

			if item["type"] == "message":
				if item["fields"]:
					dt_lines.append("**Fields:**")
					for fd in item["fields"]:
						# Render OneOf Blocks recursively visually
						if fd["is_oneof"]:
							desc_str = f" - *{fd['desc']}*" if fd.get('desc') else ""
							dt_lines.append(f"* **Oneof `{fd['name']}`**{desc_str}:")
							for o_name, o_type in fd["sub_fields"]:
								dt_lines.append(f"  * `{o_name}` ({o_type})")
						else:
							dt_lines.append(f"* `{fd['name']}` ({fd['f_type']})")
				else:
					dt_lines.append("*No fields.*")

			elif item["type"] == "enum":
				dt_lines.append("**Enum Values:**")
				sorted_items_enum = sorted(item["values"].items(), key=lambda x: x[1][0])
				for val_name, (val_num, val_desc) in sorted_items_enum:
					line = f"* `{val_name}`: {val_num}"
					if val_desc:
						line += f" - *{val_desc}*"
					dt_lines.append(line)

			dt_lines.append("") # padding inside the card

		# Close any remaining open cards at the end of the file
		while open_fences:
			dt_lines.append(open_fences.pop())

		dt_lines.append("\n---\n")

	# remove trailing separator
	if dt_lines[-1] == "\n---\n":
		dt_lines.pop(-1)

	with open(os.path.join(output_dir, "datatypes.md"), "w", encoding="utf-8") as f:
		f.write("\n".join(dt_lines))

	# --- Helper to generate payload blocks ---
	def build_payload_block(msg_name: str, label: str, is_stream: bool, skip_desc: bool = False) -> List[str]:
		stream_tag = " *(Stream)*" if is_stream else ""
		lines = [f"**{label}{stream_tag}**: *{msg_name}*"]

		msg_details = data["all_messages"].get(msg_name)
		if msg_details:
			# Print the description of the message (if we haven't already hoisted it)
			if msg_details.get("desc") and not skip_desc:
				lines.append(f"{msg_details['desc']}\n")

			if msg_details.get("fields"):
				for fd in msg_details["fields"]:
					if fd["is_oneof"]:
						desc_str = f" - *{fd['desc']}*" if fd.get('desc') else ""
						lines.append(f"* **Oneof `{fd['name']}`**{desc_str}:")
						for o_name, o_type in fd["sub_fields"]:
							lines.append(f"  * `{o_name}` ({o_type})")
					else:
						lines.append(f"* `{fd['name']}` ({fd['f_type']})")
			else:
				lines.append("* *Empty payload.*")
		else:
			lines.append("* *Empty payload.*")
		lines.append("")
		return lines

	# --- Helper to generate service files ---
	def generate_service_file(service_dict: Dict, title: str, subtitle: str, output_filename: str):
		lines: List[str] = [f"# {title}\n\n{subtitle}\n"]
		lines.extend([f":::{{contents}} {title}", ":depth: 1", ":local:", ":::"])

		sorted_services = sorted(
			service_dict.keys(),
			key=lambda k: (get_sort_key(service_dict[k]["datatype"]), k)
		)

		for name in sorted_services:
			details = service_dict[name]

			lines.append(f"(service-{name.lower()})=")
			lines.append(f"## {name}\n")
			lines.append(f"```{{admonition}} Info\n**Associated Datatype:** {{ref}}`datatype-{details['datatype'].lower()}`\n```\n")

			for rpc, rpc_info in details["rpcs"].items():
				# --- Hoisting Logic ---
				# If the RPC doesn't have a comment in the service block,
				# fetch it from the Request message block instead.
				rpc_desc = rpc_info["desc"]
				req_msg = data["all_messages"].get(rpc_info["input"])

				hoisted_req_desc = False
				if not rpc_desc and req_msg and req_msg.get("desc"):
					rpc_desc = req_msg["desc"]
					hoisted_req_desc = True # Flag to avoid double-printing in the payload block

				lines.append(f":::{{card}}")
				lines.append(f"### {rpc}")

				# remove service name in comment
				rpc_desc = rpc_desc.strip().removeprefix(rpc).strip()
				if rpc_desc:
					lines.append(f"> {rpc_desc.replace('\n', '  \n> ')}\n")

				req_label = "Request" if "Notification" not in title else "Subscription"
				resp_label = "Response" if "Notification" not in title else "Notification"

				lines.extend(build_payload_block(rpc_info["input"], req_label, rpc_info["client_streaming"], skip_desc=hoisted_req_desc))
				lines.extend(build_payload_block(rpc_info["output"], resp_label, rpc_info["server_streaming"]))
				lines.append(f":::\n")

			lines.append("---\n")

		# remove trailing separator
		if lines[-1] == "---\n":
			lines.pop(-1)

		with open(os.path.join(output_dir, output_filename), "w", encoding="utf-8") as f:
			f.write("\n".join(lines))

	# --- 2. Commands ---
	generate_service_file(data["commands"], "Commands", "", "commands.md")

	# --- 3. Notifications ---
	generate_service_file(data["notifications"], "Notifications", "Events you can subscribe to, and notification content.", "notifications.md")

	# --- 4. Admins ---
	generate_service_file(data["admins"], "Admin Commands", "Privileged commands requiring a valid admin client key.", "admins.md")

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

	parsed_data = parse_descriptor_set(descriptor_file)
	generate_markdown(parsed_data, output_dir)
	print("generate_references.py: Success")
