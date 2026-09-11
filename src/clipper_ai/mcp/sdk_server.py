"""
CLIPPER AI ASSISTANT
MCP SDK 2.2.0 Compatible Server

Adapter:
Claude Code
    |
    |
MCP stdio
    |
    |
sdk_server.py
    |
    |
tools.py
"""

from __future__ import annotations


from typing import Any, Dict, List


from mcp.server import Server

from mcp.types import (
    Tool,
    TextContent,
    ListToolsRequest,
    ListToolsResult,
    CallToolRequest,
    CallToolResult,
)


from .tools import get_tool_registry



# ==========================================================
# TOOL REGISTRY
# ==========================================================

TOOLS = get_tool_registry()



# ==========================================================
# MCP SERVER INSTANCE
# ==========================================================

server = Server(
    "CLIPPER_AI_ASSISTANT"
)



# ==========================================================
# HANDLE tools/list
# ==========================================================

async def list_tools_handler(
    context: Any,
    request: ListToolsRequest,
) -> ListToolsResult:
    """
    Return available CLIPPER tools
    to Claude Code.
    """


    tools: List[Tool] = []


    for name in TOOLS.keys():

        tools.append(

            Tool(

                name=name,

                description=(
                    f"CLIPPER AI ASSISTANT tool: {name}"
                ),

                inputSchema={

                    "type": "object",

                    "properties": {},

                    "additionalProperties": True,

                },

            )

        )


    return ListToolsResult(
        tools=tools
    )



# ==========================================================
# HANDLE tools/call
# ==========================================================

async def call_tool_handler(
    context: Any,
    request: CallToolRequest,
) -> CallToolResult:
    """
    Execute requested CLIPPER tool.
    """


    name = request.params.name


    arguments: Dict[str, Any] = (
        request.params.arguments
        or {}
    )


    if name not in TOOLS:

        raise ValueError(
            f"Unknown tool: {name}"
        )


    tool_function = TOOLS[name]


    result = tool_function(
        **arguments
    )


    # support async tool
    if hasattr(
        result,
        "__await__"
    ):

        result = await result



    return CallToolResult(

        content=[

            TextContent(

                type="text",

                text=str(result),

            )

        ]

    )



# ==========================================================
# REGISTER MCP HANDLERS
# ==========================================================

server.add_request_handler(

    "tools/list",

    ListToolsRequest,

    list_tools_handler,

)



server.add_request_handler(

    "tools/call",

    CallToolRequest,

    call_tool_handler,

)



# ==========================================================
# FACTORY
# ==========================================================

def create_mcp_server() -> Server:
    """
    Create MCP server instance.

    Used by launcher.py
    """

    return server