"""Whisper CUDA connector interface foundation."""
from typing import Dict


class WhisperCUDAConnector:
    def transcribe(self, audio_file: str) -> Dict[str, object]:
        return {
            "audio": audio_file,
            "segments": [],
            "device": "cuda",
        }
