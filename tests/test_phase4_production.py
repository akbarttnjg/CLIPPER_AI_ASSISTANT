from clipper_ai.production import (
    WhisperCUDAConnector,
    ClipDecisionEngine,
    VideoWorkflow,
)


def test_production_components():
    assert WhisperCUDAConnector().transcribe("a.wav")["device"] == "cuda"
    assert ClipDecisionEngine().select([{"score":1}])[0]["score"] == 1
    assert VideoWorkflow().execute("render")["status"] == "pipeline_ready"
