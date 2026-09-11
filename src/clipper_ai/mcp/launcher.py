"""CLIPPER AI MCP launcher."""

from .sdk_server import create_mcp_server


def main():
    server = create_mcp_server()

    if hasattr(server, "run_stdio"):
        server.run_stdio()
    elif hasattr(server, "run"):
        server.run()
    else:
        raise RuntimeError("No MCP runner found")


if __name__ == "__main__":
    main()
