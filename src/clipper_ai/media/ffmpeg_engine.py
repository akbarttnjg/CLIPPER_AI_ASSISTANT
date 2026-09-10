from pathlib import Path
import subprocess
from typing import List

def run_ffmpeg(args: List[str]) -> None:
    result = subprocess.run(
        ["ffmpeg", "-y"] + args,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)

def cut_video(source: str, output: str, start: str, end: str) -> Path:
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    run_ffmpeg([
        "-ss", start,
        "-to", end,
        "-i", source,
        "-c", "copy",
        str(out)
    ])
    if not out.exists() or out.stat().st_size == 0:
        raise RuntimeError("Invalid output video")
    return out
