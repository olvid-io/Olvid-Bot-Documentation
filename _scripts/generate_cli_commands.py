import sys
import os
sys.path.insert(0, os.path.abspath('../'))

from olvid.cli.interactive_tree import interactive_tree
from asyncclick.core import Command, Group


commands: list[Command] = interactive_tree.commands.values()

with open("../source/cli/cli_commands.rstinc", "w") as fd:
	for command in commands:
		s: str = ""

		if not isinstance(command, Group):
			print(f"WARNING: generate_cli_commands: Found a root command that is not a group: {command.name}")
			continue

		# # Create section for this group
		# s += f"{command.name.title()}\n"
		# s += f"{'-' * (len(command.name) + 2)}\n\n"

		s += f"""
.. click:: olvid.cli.handler.{command.name}_tree:{command.name}_tree
	:prog: olvid-cli {command.name}
	:nested: full
""".strip() + "\n\n"
		fd.write(s)

print("generate_cli_commands.py: Success")
