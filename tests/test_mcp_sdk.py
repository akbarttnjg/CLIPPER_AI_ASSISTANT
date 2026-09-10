from clipper_ai.mcp.sdk_server import create_mcp_server


def test_sdk_server_creation():
    server = create_mcp_server()
    assert server is not None
