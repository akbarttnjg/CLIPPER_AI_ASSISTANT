"""Claude command routing layer."""
from typing import Dict, Any


class ClaudeCommandRouter:
    def route(self, command: str) -> Dict[str, Any]:
        return {"command": command, "status": "accepted"}
