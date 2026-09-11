"""CLIPPER AI MCP SDK 2.2.0 compatible bridge."""

from typing import Any, Dict

from mcp.server import MCPServer
from .tools import get_tool_registry

TOOLS = get_tool_registry()


class ClipperMCPServer(MCPServer):
    """MCP server adapter exposing CLIPPER tools."""

    async def list_tools(self):
        result = []
        for name in TOOLS.keys():
            result.append(
                {
                    "name": name,
                    "description": f"CLIPPER tool: {name}",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                        "additionalProperties": True,
                    },
                }
            )
        return result

    async def call_tool(self, name: str, arguments: Dict[str, Any]):
        if name not in TOOLS:
            raise ValueError(f"Unknown tool: {name}")

        output = TOOLS[name](**(arguments or {}))
        return str(output)


def create_mcp_server() -> ClipperMCPServer:
    return ClipperMCPServer(
        name="CLIPPER_AI_ASSISTANT",
        version="2.0.0",
    )
