class ToolChain:
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}

    def use_tool(self, tool_name, method, *args, **kwargs):
        chosen_tool = self.tools.get(tool_name)
        if not chosen_tool:
            print(f"Tool {tool_name} not found.")
            return
        print(f"Using tool {tool_name} with method {method}")
        tool_method = getattr(chosen_tool, method, None)
        if not tool_method:
            print(f"Method {method} not found in tool {tool_name}.")
            return
        response = tool_method(*args, **kwargs)
        print(f"Tool response: {response}")
        return response
    
    def get_tool_for_command(self, command):
        for tool in self.tools.values():
            if hasattr(tool, 'commands') and command in tool.commands:
                return tool
        return None



