from pathlib import Path

def validate_release(root: str) -> bool:
    return Path(root).exists()
