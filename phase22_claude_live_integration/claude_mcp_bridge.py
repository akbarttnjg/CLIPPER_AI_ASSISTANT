class ClaudeMCPBridge:
    def connect(self) -> dict:
        return {"connected": True, "protocol": "MCP"}

    def dispatch(self, tool_name: str, arguments: dict) -> dict:
        return {"tool": tool_name, "arguments": arguments, "status": "accepted"}
