import uuid
from dataclasses import dataclass

@dataclass
class Job:
    id: str
    status: str

def create_job() -> Job:
    return Job(id=str(uuid.uuid4()), status="QUEUED")
