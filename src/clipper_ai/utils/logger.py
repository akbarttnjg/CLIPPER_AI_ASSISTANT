from pathlib import Path
from loguru import logger

def setup_logger(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger.add(str(log_dir / "clipper_ai.log"), rotation="10 MB")
