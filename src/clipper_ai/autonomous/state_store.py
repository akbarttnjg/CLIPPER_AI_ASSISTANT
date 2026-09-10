"""Persistent workflow state foundation."""
from typing import Dict, Any


class StateStore:
    def __init__(self) -> None:
        self.state: Dict[str, Any] = {}

    def save(self, key: str, value: Any) -> None:
        self.state[key] = value

    def load(self, key: str) -> Any:
        return self.state.get(key)
