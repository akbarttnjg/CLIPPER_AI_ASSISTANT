"""AI Clip Intelligence Engine."""
from dataclasses import dataclass
from typing import List


@dataclass
class ClipCandidate:
    start: float
    end: float
    score: float
    reason: str


class ClipIntelligenceEngine:
    def rank_candidates(self, candidates: List[ClipCandidate]) -> List[ClipCandidate]:
        return sorted(candidates, key=lambda x: x.score, reverse=True)
