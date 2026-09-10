from mcp.server import MCPServer

from .tools import system_check_tool, available_tools_tool


class CLIPPERMCPServer(MCPServer):
    def __init__(self) -> None:
        super().__init__(
            name="CLIPPER_AI_ASSISTANT"
        )

        self.register_tool(
            "system_check",
            system_check_tool
        )

        self.register_tool(
            "available_tools",
            available_tools_tool
        )


def create_mcp_server() -> CLIPPERMCPServer:
    return CLIPPERMCPServer()


def main() -> None:
    server = create_mcp_server()
    server.run()


if __name__ == "__main__":
    main()
