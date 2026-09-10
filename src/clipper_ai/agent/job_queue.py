"""Production job queue foundation."""
from dataclasses import dataclass
from queue import Queue
from typing import Callable, Any


@dataclass
class Job:
    name: str
    task: Callable[[], Any]


class JobQueue:
    def __init__(self) -> None:
        self.queue: Queue[Job] = Queue()

    def submit(self, job: Job) -> None:
        self.queue.put(job)

    def execute_next(self) -> Any:
        job = self.queue.get()
        return job.task()
