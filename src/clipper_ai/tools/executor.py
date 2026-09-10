"""MCP real tool executor foundation."""

from typing import Any, Dict


class ToolExecutor:
    """Dispatches validated MCP tool calls."""

    def __init__(self) -> None:
        self._tools = {}

    def register(self, name: str, handler: Any) -> None:
        self._tools[name] = handler

    def execute(self, name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if name not in self._tools:
            return {
                "success": False,
                "error": f"Unknown tool: {name}"
            }

        try:
            result = self._tools[name](payload)
            return {
                "success": True,
                "tool": name,
                "result": result
            }
        except Exception as exc:
            return {
                "success": False,
                "tool": name,
                "error": str(exc)
            }
