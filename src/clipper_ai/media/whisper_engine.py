"""Whisper transcription bridge."""

from typing import Dict
from clipper_ai.production.whisper_connector import WhisperCUDAConnector


def transcribe_video(
    video: str,
    model: str = "large-v3",
    device: str = "cuda"
) -> Dict:
    connector = WhisperCUDAConnector(
        model_name=model,
        device=device,
    )

    result = connector.transcribe(video)

    return {
        "video": str(video),
        "model": model,
        "device": device,
        "segments": result.get("segments", []),
    }


def transcribe_audio(
    audio: str,
    model: str = "large-v3",
    device: str = "cuda"
) -> Dict:
    return transcribe_video(
        video=audio,
        model=model,
        device=device,
    )
