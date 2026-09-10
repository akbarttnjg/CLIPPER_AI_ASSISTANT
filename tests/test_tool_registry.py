from clipper_ai.mcp.tools import get_available_tools


def test_tool_registry():
    result = get_available_tools()

    assert result["success"] is True
    assert result["count"] >= 5
    assert "cut_video" in [
        item["name"] for item in result["tools"]
    ]
