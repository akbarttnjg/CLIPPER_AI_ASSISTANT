"""Batch video processing coordinator."""
from typing import List, Callable


def process_batch(items: List[str], processor: Callable[[str], str]) -> List[str]:
    return [processor(item) for item in items]
