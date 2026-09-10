class RenderQueue:
    def enqueue(self, job: dict) -> dict:
        return {"state": "QUEUED", "job": job}
