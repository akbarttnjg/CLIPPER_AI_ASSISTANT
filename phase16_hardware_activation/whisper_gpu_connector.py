class WhisperGPUConnector:
    def status(self) -> dict:
        return {"backend": "cuda", "ready": False}
