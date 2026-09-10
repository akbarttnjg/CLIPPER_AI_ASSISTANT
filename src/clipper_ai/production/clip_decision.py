"""AI clip decision integration."""
from typing import List, Dict


class ClipDecisionEngine:
    def select(self, candidates: List[Dict[str, object]]) -> List[Dict[str, object]]:
        return sorted(
            candidates,
            key=lambda item: float(item.get("score", 0)),
            reverse=True,
        )
