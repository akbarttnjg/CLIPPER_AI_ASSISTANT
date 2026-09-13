"""Whisper transcription bridge."""

from typing import Dict, Optional

from clipper_ai.production.whisper_connector import (
    WhisperCUDAConnector,
)


_connector: Optional[WhisperCUDAConnector] = None


def get_connector() -> WhisperCUDAConnector:
    """
    Return reusable Whisper connector instance.

    Model is loaded once and reused to avoid
    repeated GPU VRAM allocation.
    """
    global _connector

    if _connector is None:
        _connector = WhisperCUDAConnector(
            model_name="large-v3",
            device="cuda",
            compute_type="float16",
        )

    return _connector


def transcribe_video(
    video: str,
    model: str = "large-v3",
    device: str = "cuda",
) -> Dict:

    connector = get_connector()

    result = connector.transcribe(video)

    return {
        "video": video,
        "model": model,
        "device": device,
        "segments": result.get(
            "segments",
            [],
        ),
    }


def transcribe_audio(
    audio: str,
    model: str = "large-v3",
    device: str = "cuda",
) -> Dict:

    return transcribe_video(
        video=audio,
        model=model,
        device=device,
    )