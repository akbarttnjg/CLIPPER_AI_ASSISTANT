from clipper_ai.tools.executor import ToolExecutor


def test_executor():
    executor = ToolExecutor()
    executor.register("echo", lambda p: p)
    result = executor.execute("echo", {"ok": True})
    assert result["success"] is True
