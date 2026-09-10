from typing import Dict, Callable

from clipper_ai.media.ffmpeg_engine import cut_video
from clipper_ai.media.whisper_engine import (
    transcribe_video,
    transcribe_audio,
)
from clipper_ai.subtitle.renderer import create_ass_file
from clipper_ai.davinci.fcpxml_generator import create_fcpxml


TOOLS: Dict[str, Callable] = {
    "cut_video": cut_video,
    "transcribe_video": transcribe_video,
    "transcribe_audio": transcribe_audio,
    "generate_subtitle": create_ass_file,
    "export_fcpxml": create_fcpxml,
}


def get_available_tools() -> Dict[str, object]:
    """
    Return MCP tool registry information.

    Response contract:
    {
        "success": True,
        "count": number_of_tools,
        "tools": [
            {
                "name": "tool_name"
            }
        ]
    }
    """
    return {
        "success": True,
        "count": len(TOOLS),
        "tools": [
            {"name": name}
            for name in TOOLS.keys()
        ],
    }


def get_tool_registry() -> Dict[str, Callable]:
    """
    Return the complete MCP tool registry.
    """
    return TOOLS
