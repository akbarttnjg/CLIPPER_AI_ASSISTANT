from clipper_ai.mcp.sdk_server import create_mcp_server


def test_create_mcp_server():
    server = create_mcp_server()
    assert server is not None
