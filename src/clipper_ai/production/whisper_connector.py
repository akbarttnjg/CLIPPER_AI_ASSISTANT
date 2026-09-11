"""Faster Whisper CUDA connector."""

from typing import Dict, Any, List


class WhisperCUDAConnector:
    def __init__(
        self,
        model_name: str = "large-v3",
        device: str = "cuda",
        compute_type: str = "float16",
    ):
        self.model_name = model_name
        self.device = device
        self.compute_type = compute_type
        self.model = None

    def load_model(self):
        try:
            from faster_whisper import WhisperModel
            self.model = WhisperModel(
                self.model_name,
                device=self.device,
                compute_type=self.compute_type,
            )
        except Exception:
            from faster_whisper import WhisperModel
            self.model = WhisperModel(
                self.model_name,
                device="cpu",
                compute_type="int8",
            )

    def transcribe(self, audio_file: str) -> Dict[str, Any]:
        if self.model is None:
            self.load_model()

        segments, info = self.model.transcribe(audio_file)

        result: List[Dict[str, Any]] = []

        for segment in segments:
            result.append({
                "start": float(segment.start),
                "end": float(segment.end),
                "text": segment.text.strip(),
            })

        return {
            "audio": audio_file,
            "language": getattr(info, "language", None),
            "segments": result,
            "device": self.device,
        }
