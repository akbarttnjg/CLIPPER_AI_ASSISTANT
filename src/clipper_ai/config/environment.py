from pathlib import Path
from dotenv import load_dotenv
import os


def load_environment(env_path: Path | None = None) -> None:
    if env_path is None:
        env_path = Path.cwd() / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def get_env(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)
