import json

from .sdk_server import create_mcp_server


def main() -> None:
    server = create_mcp_server()

    print("CLIPPER_AI_ASSISTANT MCP SERVER")
    print("==============================")
    print(json.dumps({
        "status": "READY",
        "server": "CLIPPER_AI_ASSISTANT",
        "protocol": "MCP"
    }, indent=2))


if __name__ == "__main__":
    main()
