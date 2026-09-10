from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_name: str = "CLIPPER_AI_ASSISTANT"
    version: str = "1.0.0"

settings = Settings()
