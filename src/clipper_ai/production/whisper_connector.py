"""
Faster Whisper CUDA connector.

Features:
- Thread-safe singleton lifecycle
- Lazy GPU model loading
- CUDA float16 optimized
- CPU int8 fallback
- Word-level timestamps
- Normalized transcription schema
- Explicit GPU memory release
"""

from __future__ import annotations

import gc
from threading import Lock
from typing import Any, Dict, List, Optional


class WhisperCUDAConnector:
    """
    Thread-safe Faster Whisper connector.

    The Whisper model is loaded lazily only once.
    """

    def __init__(
        self,
        model_name: str = "large-v3",
        device: str = "cuda",
        compute_type: str = "float16",
    ) -> None:

        self.model_name: str = model_name
        self.requested_device: str = device
        self.compute_type: str = compute_type

        self.model: Optional[Any] = None

        self.active_device: Optional[str] = None

        self._lock: Lock = Lock()


    def load_model(self) -> None:
        """
        Load Whisper model lazily.

        Loading priority:
        1. CUDA float16
        2. CPU int8 fallback
        """

        if self.model is not None:
            print("[WHISPER] Reusing existing model")
            return


        with self._lock:

            if self.model is not None:
                print("[WHISPER] Reusing existing model")
                return


            from faster_whisper import WhisperModel


            try:

                print(
                    f"[WHISPER] Loading "
                    f"{self.model_name} "
                    f"on {self.requested_device} "
                    f"({self.compute_type})"
                )


                self.model = WhisperModel(
                    self.model_name,
                    device=self.requested_device,
                    compute_type=self.compute_type,
                )


                self.active_device = self.requested_device


                print(
                    "[WHISPER] Model loaded successfully"
                )


            except Exception as error:

                print(
                    "[WHISPER] CUDA initialization failed"
                )

                print(
                    f"[WHISPER] Reason: {error}"
                )

                print(
                    "[WHISPER] Loading CPU int8 fallback"
                )


                self.model = WhisperModel(
                    self.model_name,
                    device="cpu",
                    compute_type="int8",
                )


                self.active_device = "cpu"


                print(
                    "[WHISPER] CPU model loaded successfully"
                )


    def transcribe(
        self,
        audio_file: str,
    ) -> Dict[str, Any]:
        """
        Transcribe audio/video source.

        Args:
            audio_file:
                Path to media file.

        Returns:
            Normalized transcription dictionary.
        """


        if self.model is None:

            self.load_model()


        if self.model is None:

            raise RuntimeError(
                "Whisper model initialization failed"
            )


        segments, info = self.model.transcribe(
            audio_file,
            beam_size=5,
            word_timestamps=True,
            vad_filter=True,
            condition_on_previous_text=False,
        )


        normalized_segments: List[
            Dict[str, Any]
        ] = []


        for segment in segments:

            words: List[
                Dict[str, Any]
            ] = []


            if segment.words:

                for word in segment.words:

                    words.append(
                        {
                            "word": (
                                word.word.strip()
                            ),
                            "start": (
                                float(word.start)
                            ),
                            "end": (
                                float(word.end)
                            ),
                        }
                    )


            normalized_segments.append(
                {
                    "start": (
                        float(segment.start)
                    ),
                    "end": (
                        float(segment.end)
                    ),
                    "text": (
                        segment.text.strip()
                    ),
                    "words": words,
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

            "device": self.active_device,

        }



    def release(self) -> None:
        """
        Release Whisper model and GPU cache.

        Used when application shutdown
        or when GPU memory must be reclaimed.
        """

        with self._lock:

            self.model = None

            self.active_device = None

            gc.collect()


            try:

                import torch


                if torch.cuda.is_available():

                    torch.cuda.empty_cache()

                    torch.cuda.ipc_collect()


            except ImportError:

                print(
                    "[WHISPER] Torch unavailable"
                )


            except Exception as error:

                print(
                    "[WHISPER] CUDA cleanup warning:"
                )

                print(error)


        print(
            "[WHISPER] Resources released"
        )



# =====================================================
# GLOBAL SINGLETON INSTANCE
# =====================================================


_connector_instance: Optional[
    WhisperCUDAConnector
] = None


_connector_lock: Lock = Lock()



def get_connector(
    model_name: str = "large-v3",
    device: str = "cuda",
    compute_type: str = "float16",
) -> WhisperCUDAConnector:
    """
    Return global Whisper connector.

    Guarantees:
    - one model instance
    - one GPU allocation
    - shared lifecycle
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