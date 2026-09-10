from clipper_ai.integration import EndToEndPipeline, IntegrationJob


def test_full_pipeline():
    result = EndToEndPipeline().execute(
        IntegrationJob("sample.mp4")
    )

    assert result.state["completed"] is True
    assert result.state["ffmpeg_ready"] is True
