"""CLIPPER AI MCP SDK 2.2 compatible server."""
from typing import Any, Dict, Optional
from .tools import get_tool_registry

TOOLS = get_tool_registry()

class ClipperMCPServer:
    def __init__(self):
        self.name = "CLIPPER_AI_ASSISTANT"
        self.version = "7.0.0"

    async def list_tools(self):
        return [
            {
                "name": name,
                "description": f"CLIPPER tool: {name}",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": True,
                },
            }
            for name in TOOLS
        ]

    async def call_tool(
        self,
        name: str,
        arguments: Optional[Dict[str, Any]] = None,
        context: Any = None,
    ):
        if name not in TOOLS:
            raise ValueError(f"Unknown tool: {name}")

        result = TOOLS[name](**(arguments or {}))
        return {
            "content": [
                {
                    "type": "text",
                    "text": str(result),
                }
            ]
        }

def create_mcp_server():
    return ClipperMCPServer()
