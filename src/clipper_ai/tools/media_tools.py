"""Initial media MCP tools."""

from typing import Any, Dict


def video_probe(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "status": "READY",
        "input": payload.get("input"),
        "duration": 0,
        "note": "FFmpeg probe connector ready"
    }


def extract_audio(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "status": "READY",
        "input": payload.get("input"),
        "note": "Audio extraction connector ready"
    }
