"""Pipeline progress tracking."""
from dataclasses import dataclass


@dataclass
class ProgressState:
    stage: str
    percent: float


class ProgressTracker:
    def __init__(self) -> None:
        self.state = ProgressState("idle", 0.0)

    def update(self, stage: str, percent: float) -> ProgressState:
        self.state = ProgressState(stage, percent)
        return self.state
