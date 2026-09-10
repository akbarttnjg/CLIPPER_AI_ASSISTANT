from pathlib import Path


class WorkspacePaths:
    def __init__(self, root: Path):
        self.root = root
        self.projects = root / "projects"
        self.cache = root / "cache"
        self.logs = root / "logs"
        self.temp = root / "temp"

    def create(self) -> None:
        for path in [
            self.root,
            self.projects,
            self.cache,
            self.logs,
            self.temp,
        ]:
            path.mkdir(parents=True, exist_ok=True)
