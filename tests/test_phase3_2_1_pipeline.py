from clipper_ai.pipeline import (
    PipelineJob,
    PipelineOrchestrator,
    validate_input,
    prepare_media,
    finalize_job,
)


def test_pipeline_orchestrator():
    pipeline = PipelineOrchestrator()
    pipeline.register_stage(validate_input)
    pipeline.register_stage(prepare_media)
    pipeline.register_stage(finalize_job)

    result = pipeline.execute(
        PipelineJob(job_id="test-001", input_file="sample.mp4")
    )

    assert result.metadata["completed"] is True
