class CommandParser:
    def __init__(self, toolchain):
        self.toolchain = toolchain

    def parse(self, command):
        command_parts = command.split(' ')
        command_name = command_parts[0]
        command_args = command_parts[1:]

        tool = self.toolchain.get_tool_for_command(command_name)
        if tool is None:
            print(f"Unknown command: {command_name}")
            return

        # Retrieve the specific command for the tool
        tool_method = None
        for name, (description, method) in tool.commands.items():
            if name == command_name:
                tool_method = method
                break

        if not tool_method:
            print(f"Method {command_name} not found in tool {tool.name}.")
            return

        return tool_method(*command_args)

    @classmethod
    def list_commands(cls, toolchain):
        # Print all commands and their descriptions
        for tool in toolchain.tools.values():
            for command, (description, method) in tool.commands.items():
                print(f"{command}: {description}") 
