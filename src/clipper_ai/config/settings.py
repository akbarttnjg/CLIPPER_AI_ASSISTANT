from pathlib import Path
from dataclasses import dataclass
from .environment import load_environment, get_env
from .paths import WorkspacePaths


load_environment()


@dataclass(frozen=True)
class Settings:
    project_name: str
    project_root: Path
    workspace_root: Path
    ffmpeg_path: str
    whisper_model: str
    whisper_device: str
    davinci_auto_import: bool

    @property
    def workspace(self) -> WorkspacePaths:
        return WorkspacePaths(self.workspace_root)

    def validate(self) -> list[str]:
        errors = []

        if not self.project_root.exists():
            errors.append(f"Missing project root: {self.project_root}")

        return errors


settings = Settings(
    project_name=get_env("PROJECT_NAME", "CLIPPER_AI_ASSISTANT"),
    project_root=Path(
        get_env("PROJECT_ROOT", r"C:\CLIPPER_AI_ASSISTANT")
    ),
    workspace_root=Path(
        get_env("WORKSPACE_PATH", r"C:\CLIPPER_WORKSPACE")
    ),
    ffmpeg_path=get_env(
        "FFMPEG_PATH",
        r"C:fmpeginfmpeg.exe"
    ),
    whisper_model=get_env(
        "WHISPER_MODEL",
        "large-v3"
    ),
    whisper_device=get_env(
        "WHISPER_DEVICE",
        "cuda"
    ),
    davinci_auto_import=(
        get_env("DAVINCI_AUTO_IMPORT", "true").lower() == "true"
    ),
)


if __name__ == "__main__":
    print("CLIPPER_AI_ASSISTANT CONFIG")
    print("---------------------------")
    print(f"Project : {settings.project_name}")
    print(f"Root    : {settings.project_root}")
    print(f"Workspace: {settings.workspace_root}")
    print(f"Whisper : {settings.whisper_model}")
    print(f"Device  : {settings.whisper_device}")

    errors = settings.validate()

    if errors:
        print("CONFIG ERRORS")
        for error in errors:
            print("-", error)
    else:
        print("CONFIG OK")
