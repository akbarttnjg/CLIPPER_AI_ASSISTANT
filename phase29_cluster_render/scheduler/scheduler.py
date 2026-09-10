from typing import List, Dict

class RenderScheduler:
    def __init__(self):
        self.jobs: List[Dict] = []

    def submit(self, job: Dict) -> None:
        self.jobs.append(job)

    def pending(self) -> int:
        return len(self.jobs)
