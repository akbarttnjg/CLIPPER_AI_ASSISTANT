def send_pipeline_job(payload: dict) -> dict:
    return {"pipeline": "queued", "payload": payload}
