from .server import create_server


def main() -> None:
    server = create_server()

    print("CLIPPER_AI_ASSISTANT MCP CORE")
    print("============================")

    result = server.execute("check_system")

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
