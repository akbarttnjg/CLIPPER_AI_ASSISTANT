"""
FFmpeg NVENC subtitle burn renderer.

Responsibilities:
- Burn ASS subtitle using libass
- Encode with NVIDIA NVENC
- Preserve audio
- Validate output
- Safe subprocess handling
"""


from __future__ import annotations

import subprocess
import shlex

from pathlib import Path
from typing import List



class FFmpegRenderError(Exception):
    """
    FFmpeg execution failure.
    """
    pass



def escape_filter_path(
    path: str,
) -> str:
    """
    Escape Windows path for FFmpeg filter.

    Example:

    C:\video\a.ass

    becomes:

    C\\:/video/a.ass
    """

    value = str(
        Path(path)
        .absolute()
    )


    value = value.replace(
        "\\",
        "/"
    )


    value = value.replace(
        ":",
        "\\:"
    )


    return value




def run_ffmpeg(
    command: List[str],
) -> None:
    """
    Execute FFmpeg safely.

    Raises:
        FFmpegRenderError
    """


    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


    stdout, stderr = process.communicate()


    if process.returncode != 0:

        raise FFmpegRenderError(
            "\nFFmpeg failed\n\n"
            + stderr[-4000:]
        )





def render_with_ass_nvenc(
    input_video: str,
    subtitle_file: str,
    output_video: str,
    preset: str = "p5",
) -> str:
    """
    Burn ASS subtitle and encode using NVENC.


    Args:

        input_video:
            source mp4

        subtitle_file:
            generated ASS subtitle

        output_video:
            final mp4


        preset:
            NVENC preset


    Returns:

        output path
    """



    source = Path(
        input_video
    )


    subtitle = Path(
        subtitle_file
    )


    output = Path(
        output_video
    )



    if not source.exists():

        raise FileNotFoundError(
            f"Input video missing: {source}"
        )


    if not subtitle.exists():

        raise FileNotFoundError(
            f"ASS subtitle missing: {subtitle}"
        )



    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )



    ass_path = escape_filter_path(
        str(subtitle)
    )


    video_filter = (
        f"subtitles='{ass_path}'"
    )



    command = [

        "ffmpeg",

        "-y",

        "-i",
        str(source),


        "-vf",
        video_filter,


        # NVIDIA encoder

        "-c:v",
        "h264_nvenc",


        "-preset",
        preset,


        "-rc",
        "vbr",


        "-cq",
        "19",


        "-b:v",
        "0",


        # audio

        "-c:a",
        "aac",

        "-b:a",
        "192k",


        "-movflags",
        "+faststart",


        str(output),

    ]



    print(
        "[FFMPEG] Starting NVENC render"
    )


    print(
        " ".join(
            shlex.quote(x)
            for x in command
        )
    )



    run_ffmpeg(
        command
    )



    if not output.exists():

        raise RuntimeError(
            "Output video not created"
        )


    if output.stat().st_size <= 0:

        raise RuntimeError(
            "Output video empty"
        )


    print(
        "[FFMPEG] Render complete"
    )


    return str(output)





if __name__ == "__main__":


    print(
        "FFmpeg NVENC renderer module OK"
    )