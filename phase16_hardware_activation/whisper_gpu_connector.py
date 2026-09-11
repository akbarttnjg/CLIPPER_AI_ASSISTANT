class WhisperGPUConnector:
    def status(self) -> dict:
        return {
            "backend": "cuda",
            "ready": True,
            "model": "large-v3",
            "compute_type": "float16",
        }
