class WorkflowExecutor:
    def execute(self, workflow: dict) -> dict:
        return {"workflow": workflow, "status": "queued"}
