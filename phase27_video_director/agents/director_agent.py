from typing import Dict, Any

class VideoDirectorAgent:
    def create_plan(self, request: str) -> Dict[str, Any]:
        return {"request": request, "steps": ["analyze", "edit", "render"]}
