from typing import Any, Dict

from mcp.server import MCPServer

from .tools import get_available_tools


def create_mcp_server() -> MCPServer:
    server = MCPServer(
        name="CLIPPER_AI_ASSISTANT",
        version="0.1.0",
    )

    @server.tool()
    def system_check() -> Dict[str, Any]:
        return {
            "success": True,
            "message": "CLIPPER_AI_ASSISTANT MCP Server ready",
        }

    @server.tool()
    def available_tools() -> Dict[str, Any]:
        return get_available_tools()

    return server
