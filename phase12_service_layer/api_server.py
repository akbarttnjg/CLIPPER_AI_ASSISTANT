from .job_controller import create_job

def health() -> dict:
    return {"status": "READY"}

def submit_job() -> dict:
    job = create_job()
    return {"job_id": job.id}
