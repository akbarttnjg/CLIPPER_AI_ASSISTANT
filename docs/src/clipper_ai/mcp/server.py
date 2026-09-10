from .tools import check_system, list_tools


class MCPServer:
    def __init__(self) -> None:
        self.tools = {
            "check_system": check_system,
            "list_tools": list_tools,
        }

    def execute(self, tool_name: str):
        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name}")

        return self.tools[tool_name]()


def create_server() -> MCPServer:
    return MCPServer()
