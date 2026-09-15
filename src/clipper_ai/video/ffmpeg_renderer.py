"""
FFmpeg NVENC Renderer.

Features:
- ASS subtitle burn-in using libass
- NVIDIA NVENC H264 encoding
- Windows path safe escaping
- Robust subprocess handling
- Output validation
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import List


class FFmpegRenderError(Exception):
    """
    FFmpeg rendering exception.
    """



def escape_filter_path(path: Path) -> str:
    """
    Convert Windows path into FFmpeg subtitles filter safe path.

    Example:

    C:\\video\\subtitle.ass

    becomes:

    C\\:/video/subtitle.ass
    """

    value: str = str(path.resolve())

    # Windows slash -> FFmpeg slash
    value = value.replace("\\", "/")

    # Escape drive colon
    value = value.replace(":", "\\:")

    return value



def run_ffmpeg(
    command: List[str],
) -> None:
    """
    Execute FFmpeg process safely.

    Args:
        command:
            Complete FFmpeg command.

    Raises:
        FFmpegRenderError
    """

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


    stdout, stderr = process.communicate()


    if process.returncode != 0:

        raise FFmpegRenderError(
            "\n".join(
                [
                    "FFmpeg execution failed",
                    "",
                    stderr[-8000:],
                ]
            )
        )



def validate_output(
    output_file: Path,
) -> None:
    """
    Validate generated media file.

    Checks:
    - file exists
    - file size > 0
    """

    if not output_file.exists():

        raise FFmpegRenderError(
            f"Output not created: {output_file}"
        )


    size = output_file.stat().st_size


    if size <= 0:

        raise FFmpegRenderError(
            "Output file is empty"
        )


    print(
        f"[FFMPEG] Output size: {size / 1024 / 1024:.2f} MB"
    )



def render_with_ass_nvenc(
    input_video: str,
    subtitle_file: str,
    output_video: str,
    overwrite: bool = True,
) -> Path:
    """
    Burn ASS subtitle and encode with NVENC.

    Args:

        input_video:
            Source MP4.

        subtitle_file:
            ASS subtitle file.

        output_video:
            Destination MP4.

    Returns:

        Generated output path.
    """


    source = Path(input_video)

    subtitle = Path(subtitle_file)

    output = Path(output_video)



    if not source.exists():

        raise FileNotFoundError(
            f"Missing input video: {source}"
        )


    if not subtitle.exists():

        raise FileNotFoundError(
            f"Missing subtitle: {subtitle}"
        )


    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )



    subtitle_path = escape_filter_path(
        subtitle
    )


    vf_filter = (
        f"subtitles='{subtitle_path}'"
    )



    command: List[str] = [

        "ffmpeg",

        "-hide_banner",

        "-loglevel",
        "error",

        "-stats",


        "-y" if overwrite else "-n",


        "-i",
        str(source),


        "-vf",
        vf_filter,


        # =========================
        # NVIDIA NVENC
        # =========================

        "-c:v",
        "h264_nvenc",

        "-preset",
        "p4",

        "-profile:v",
        "high",

        "-rc",
        "vbr",

        "-cq",
        "23",

        "-pix_fmt",
        "yuv420p",


        # =========================
        # Audio
        # =========================

        "-c:a",
        "aac",

        "-b:a",
        "192k",


        # =========================
        # Streaming optimization
        # =========================

        "-movflags",
        "+faststart",


        str(output),

    ]



    print(
        "[FFMPEG] Command:"
    )

    print(
        " ".join(command)
    )



    run_ffmpeg(
        command
    )


    validate_output(
        output
    )


    print(
        "[FFMPEG] Render complete"
    )


    return output



# ==========================================================
# CLI TEST
# ==========================================================

if __name__ == "__main__":

    import sys


    if len(sys.argv) != 4:

        print(
            """
Usage:

python ffmpeg_renderer.py input.mp4 subtitle.ass output.mp4

Example:

python ffmpeg_renderer.py video.mp4 subtitle.ass result.mp4
"""
        )

        raise SystemExit(1)



    render_with_ass_nvenc(

        input_video=sys.argv[1],

        subtitle_file=sys.argv[2],

        output_video=sys.argv[3],

    )