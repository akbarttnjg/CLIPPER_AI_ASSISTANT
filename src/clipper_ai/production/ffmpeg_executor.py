"""Real FFmpeg media job executor foundation."""
from dataclasses import dataclass
from pathlib import Path
from typing import List
import subprocess


@dataclass
class MediaJob:
    input_video: Path
    output_video: Path


class FFmpegExecutor:
    def run(self, job: MediaJob) -> bool:
        command: List[str] = [
            "ffmpeg",
            "-y",
            "-i",
            str(job.input_video),
            "-c",
            "copy",
            str(job.output_video),
        ]
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.returncode == 0
