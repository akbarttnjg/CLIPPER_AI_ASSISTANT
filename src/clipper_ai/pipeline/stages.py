"""Default pipeline stages."""

from .orchestrator import PipelineJob


def validate_input(job: PipelineJob) -> PipelineJob:
    job.metadata["validated"] = True
    return job


def prepare_media(job: PipelineJob) -> PipelineJob:
    job.metadata["media_prepared"] = True
    return job


def finalize_job(job: PipelineJob) -> PipelineJob:
    job.metadata["completed"] = True
    return job
