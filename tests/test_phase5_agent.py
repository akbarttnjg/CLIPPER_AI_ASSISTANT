from clipper_ai.agent import JobQueue, Job, ProgressTracker


def test_phase5_agent_layer():
    queue = JobQueue()
    queue.submit(Job("test", lambda: "ok"))
    assert queue.execute_next() == "ok"

    tracker = ProgressTracker()
    assert tracker.update("render", 50).percent == 50
