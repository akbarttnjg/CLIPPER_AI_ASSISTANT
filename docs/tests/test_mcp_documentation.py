from clipper_ai.mcp.server import create_server


def test_mcp_core():
    server = create_server()

    result = server.execute("list_tools")

    assert result.success is True
    assert "check_system" in result.data["tools"]
