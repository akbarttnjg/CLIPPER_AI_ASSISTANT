"""Error recovery layer."""
from typing import Callable, TypeVar

T = TypeVar("T")


def safe_execute(operation: Callable[[], T]) -> T:
    try:
        return operation()
    except Exception as exc:
        raise RuntimeError(f"Pipeline recovery failed: {exc}") from exc
