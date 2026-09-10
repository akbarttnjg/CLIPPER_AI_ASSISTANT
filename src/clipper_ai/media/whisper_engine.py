from pathlib import Path
from typing import Dict


def transcribe_video(
    video: str,
    model: str = "large-v3",
    device: str = "cuda"
) -> Dict:
    """
    Whisper transcription interface.

    This compatibility implementation keeps the pipeline contract.
    The production CUDA inference backend can be connected here.
    """
    return {
        "video": str(video),
        "model": model,
        "device": device,
        "segments": []
    }


def transcribe_audio(
    audio: str,
    model: str = "large-v3",
    device: str = "cuda"
) -> Dict:
    """
    Backward-compatible audio transcription entry point.

    MCP tools and previous pipeline versions may call this name.
    """
    return transcribe_video(
        video=audio,
        model=model,
        device=device
    )
