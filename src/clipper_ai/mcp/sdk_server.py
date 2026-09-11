"""
CLIPPER AI ASSISTANT
MCP SDK 2.2.0 Server Adapter

Version:
v7.1 Tool Schema Layer

Purpose:
- Expose CLIPPER tools to Claude Code
- Provide correct JSON schema
- Execute registered tools safely
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



# ============================================================
# TOOL REGISTRY
# ============================================================

TOOLS: Dict[str, Dict[str, Any]] = (
    get_tool_registry()
)



# ============================================================
# MCP SERVER INSTANCE
# ============================================================

server = Server(
    "CLIPPER_AI_ASSISTANT"
)



# ============================================================
# tools/list HANDLER
# ============================================================

async def list_tools_handler(
    context: Any,
    request: ListToolsRequest,
) -> ListToolsResult:
    """
    Return available tools and their schemas.
    """

    tools: List[Tool] = []


    for name, definition in TOOLS.items():

        tools.append(

            Tool(

                name=name,

                description=(
                    f"CLIPPER AI ASSISTANT tool: {name}"
                ),

                inputSchema=(
                    definition.get(
                        "schema",
                        {
                            "type": "object",
                            "properties": {},
                        },
                    )
                ),

            )

        )


    return ListToolsResult(
        tools=tools
    )



# ============================================================
# tools/call HANDLER
# ============================================================

async def call_tool_handler(
    context: Any,
    request: CallToolRequest,
) -> CallToolResult:
    """
    Execute requested MCP tool.
    """


    tool_name = request.params.name


    arguments: Dict[str, Any] = (
        request.params.arguments
        or {}
    )


    if tool_name not in TOOLS:

        raise ValueError(
            f"Unknown tool: {tool_name}"
        )


    definition = TOOLS[tool_name]


    handler = definition.get(
        "handler"
    )


    if handler is None:

        raise RuntimeError(
            f"Tool {tool_name} has no handler"
        )


    result = handler(
        **arguments
    )


    # Support async tools
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



# ============================================================
# REGISTER MCP METHODS
# ============================================================

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



# ============================================================
# FACTORY
# ============================================================

def create_mcp_server() -> Server:
    """
    Return configured MCP server instance.
    """

    return server