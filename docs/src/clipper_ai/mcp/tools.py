from clipper_ai.config import settings
from .schemas import ToolResponse


def check_system() -> ToolResponse:
    errors = settings.validate()

    if errors:
        return ToolResponse(
            success=False,
            message="System check failed",
            data={"errors": errors},
        )

    return ToolResponse(
        success=True,
        message="CLIPPER_AI_ASSISTANT system ready",
        data={
            "project": settings.project_name,
            "workspace": str(settings.workspace_root),
            "whisper_model": settings.whisper_model,
            "whisper_device": settings.whisper_device,
        },
    )


def list_tools() -> ToolResponse:
    return ToolResponse(
        success=True,
        message="Available MCP tools",
        data={
            "tools": [
                "check_system",
                "list_tools",
            ]
        },
    )
