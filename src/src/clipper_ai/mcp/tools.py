from clipper_ai.config import settings


def system_check_tool() -> dict:
    errors = settings.validate()

    if errors:
        return {
            "success": False,
            "message": "System check failed",
            "errors": errors,
        }

    return {
        "success": True,
        "message": "CLIPPER_AI_ASSISTANT MCP ready",
        "data": {
            "project": settings.project_name,
            "workspace": str(settings.workspace_root),
            "whisper_model": settings.whisper_model,
            "device": settings.whisper_device,
        },
    }


def available_tools_tool() -> dict:
    return {
        "success": True,
        "tools": [
            "system_check",
            "available_tools",
        ],
    }
