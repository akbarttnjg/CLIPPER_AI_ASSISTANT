"""
Faster Whisper CUDA connector.

Responsibilities:
- Manage singleton WhisperModel lifecycle
- Lazy-load model only once
- Prevent duplicate GPU allocation
- Provide normalized transcription output
"""

from __future__ import annotations

from threading import Lock
from typing import Any, Dict, List, Optional


class WhisperCUDAConnector:
    """
    Singleton-friendly Faster Whisper connector.

    Model is loaded lazily on first transcription request.
    """

    def __init__(
        self,
        model_name: str = "large-v3",
        device: str = "cuda",
        compute_type: str = "float16",
    ) -> None:
        self.model_name: str = model_name
        self.device: str = device
        self.compute_type: str = compute_type

        self.model: Optional[Any] = None

        self._lock: Lock = Lock()


    def load_model(self) -> None:
        """
        Load Whisper model exactly once.

        Priority:
        1. CUDA float16
        2. CPU int8 fallback
        """

        if self.model is not None:
            return

        with self._lock:

            # double-check after acquiring lock
            if self.model is not None:
                return

            try:
                from faster_whisper import WhisperModel

                print(
                    f"[WHISPER] Loading {self.model_name} "
                    f"on {self.device} ({self.compute_type})"
                )

                self.model = WhisperModel(
                    self.model_name,
                    device=self.device,
                    compute_type=self.compute_type,
                )

                print("[WHISPER] Model loaded successfully")

            except Exception as error:

                print(
                    "[WHISPER] CUDA initialization failed."
                    f" Falling back CPU. Reason: {error}"
                )

                from faster_whisper import WhisperModel

                self.model = WhisperModel(
                    self.model_name,
                    device="cpu",
                    compute_type="int8",
                )

                print("[WHISPER] CPU fallback model loaded")


    def transcribe(
        self,
        audio_file: str,
    ) -> Dict[str, Any]:
        """
        Execute transcription.

        Args:
            audio_file:
                Path to audio/video file.

        Returns:
            Dictionary containing:
            - audio
            - language
            - segments
            - device
        """

        if self.model is None:
            self.load_model()


        if self.model is None:
            raise RuntimeError(
                "Whisper model initialization failed"
            )


        segments, info = self.model.transcribe(
            audio_file
        )


        normalized_segments: List[Dict[str, Any]] = []


        for segment in segments:

            normalized_segments.append(
                {
                    "start": float(segment.start),
                    "end": float(segment.end),
                    "text": segment.text.strip(),
                }
            )


        return {
            "audio": audio_file,
            "language": getattr(
                info,
                "language",
                None,
            ),
            "segments": normalized_segments,
            "device": self.device,
        }



# ============================================================
# GLOBAL SINGLETON INSTANCE
# ============================================================

_connector_instance: Optional[WhisperCUDAConnector] = None

_connector_lock: Lock = Lock()



def get_connector(
    model_name: str = "large-v3",
    device: str = "cuda",
    compute_type: str = "float16",
) -> WhisperCUDAConnector:
    """
    Return global Whisper connector instance.

    The same object is reused across the application.
    """

    global _connector_instance


    if _connector_instance is not None:
        return _connector_instance


    with _connector_lock:

        if _connector_instance is None:

            _connector_instance = WhisperCUDAConnector(
                model_name=model_name,
                device=device,
                compute_type=compute_type,
            )


    return _connector_instance