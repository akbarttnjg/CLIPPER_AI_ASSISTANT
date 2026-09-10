class ClaudeToolRouter:
    def route(self, command: str) -> dict:
        return {"command": command, "route": "pipeline"}
