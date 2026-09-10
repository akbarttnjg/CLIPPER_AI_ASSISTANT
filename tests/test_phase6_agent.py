from clipper_ai.autonomous import AutonomousVideoAgent, StateStore


def test_phase6_autonomous_agent():
    agent = AutonomousVideoAgent()
    result = agent.run({"video": "input.mp4"})
    assert result.status == "READY"

    store = StateStore()
    store.save("job", "ok")
    assert store.load("job") == "ok"
