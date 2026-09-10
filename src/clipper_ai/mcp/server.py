from typing import Dict


def create_server() -> Dict[str, str]:
    """
    Create MCP server descriptor.

    Returns:
        MCP server metadata.
    """
    return {
        "name": "clipper-ai-mcp",
        "status": "ready",
    }
