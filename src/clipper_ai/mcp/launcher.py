"""
CLIPPER AI ASSISTANT
MCP SDK 2.2.0 STDIO Launcher
"""

from __future__ import annotations

import asyncio
import traceback

from mcp.server.stdio import stdio_server


from .sdk_server import create_mcp_server



async def main() -> None:
    """
    Start MCP server menggunakan stdio transport.
    """

    server = create_mcp_server()


    try:

        async with stdio_server() as (
            read_stream,
            write_stream,
        ):

            await server.run(

                read_stream,

                write_stream,

                server.create_initialization_options(),

            )


    except Exception:

        traceback.print_exc()

        raise



if __name__ == "__main__":

    asyncio.run(main())