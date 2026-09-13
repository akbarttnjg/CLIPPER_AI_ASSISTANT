"""
ASS subtitle renderer for TikTok/Reels style clips.

Responsibilities:
- Convert Whisper word timestamps into ASS dialogue events
- Smart wrapping
- Word highlight animation
- Vertical video subtitle layout
- Generate valid ASS subtitle file
"""


from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


# ============================================================
# TIME FORMAT
# ============================================================


def seconds_to_ass_time(seconds: float) -> str:
    """
    Convert seconds to ASS timestamp.

    ASS format:
    H:MM:SS.cc
    """

    hours = int(seconds // 3600)

    minutes = int(
        (seconds % 3600) // 60
    )

    secs = int(
        seconds % 60
    )

    centiseconds = int(
        (seconds - int(seconds)) * 100
    )


    return (
        f"{hours}:"
        f"{minutes:02d}:"
        f"{secs:02d}."
        f"{centiseconds:02d}"
    )



# ============================================================
# SMART WRAPPING
# ============================================================


def smart_wrap_words(
    words: List[Dict[str, Any]],
    max_words: int = 4,
) -> List[List[Dict[str, Any]]]:
    """
    Split words into subtitle groups.

    Example:

    input:
    10 words

    output:
    [
      [word1,word2,word3,word4],
      [word5,word6,word7,word8],
      [word9,word10]
    ]
    """

    result: List[
        List[Dict[str, Any]]
    ] = []


    buffer: List[
        Dict[str, Any]
    ] = []


    for word in words:

        buffer.append(word)


        if len(buffer) >= max_words:

            result.append(buffer)

            buffer = []


    if buffer:

        result.append(buffer)


    return result



# ============================================================
# ASS HEADER
# ============================================================


def build_ass_header() -> str:
    """
    Create ASS header.
    """


    return """
[Script Info]
Title: CLIPPER AI TikTok Subtitle
ScriptType: v4.00+
WrapStyle: 2
ScaledBorderAndShadow: yes
PlayResX: 1080
PlayResY: 1920


[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding

Style: TikTokViral,Arial,90,&H00FFFFFF,&H0000FFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,6,3,2,80,80,350,1


[Events]
Format: Layer,Start,End,Style,Text
""".strip()



# ============================================================
# WORD HIGHLIGHT
# ============================================================


def build_highlight_text(
    words: List[Dict[str, Any]],
) -> str:
    """
    Create ASS karaoke-like word highlight.

    Active words use yellow.
    """


    output: List[str] = []


    for word in words:

        text = (
            word["word"]
            .strip()
        )


        if not text:
            continue


        duration = (
            word["end"]
            -
            word["start"]
        )


        karaoke = max(
            1,
            int(duration * 100)
        )


        output.append(
            f"{{\\k{karaoke}}}{text}"
        )


    return " ".join(output)



# ============================================================
# DIALOGUE BUILDER
# ============================================================


def build_dialogue(
    words: List[Dict[str, Any]],
) -> str:
    """
    Create ASS Dialogue line.
    """


    if not words:
        return ""


    start = words[0]["start"]

    end = words[-1]["end"]


    text = build_highlight_text(
        words
    )


    return (
        "Dialogue: 0,"
        f"{seconds_to_ass_time(start)},"
        f"{seconds_to_ass_time(end)},"
        "TikTokViral,"
        f"{text}"
    )



# ============================================================
# MAIN RENDERER
# ============================================================


def render_ass(
    segments: List[Dict[str, Any]],
    output_file: str,
) -> str:
    """
    Render ASS subtitle.

    Args:

        segments:
            Whisper normalized segments.

        output_file:
            Destination .ass path.


    Returns:

        Created file path
    """


    lines: List[str] = []

    lines.append(
        build_ass_header()
    )


    for segment in segments:


        words = segment.get(
            "words",
            []
        )


        if not words:
            continue



        groups = smart_wrap_words(
            words
        )


        for group in groups:


            dialogue = build_dialogue(
                group
            )


            if dialogue:

                lines.append(
                    dialogue
                )



    content = (
        "\n\n".join(lines)
        +
        "\n"
    )


    path = Path(
        output_file
    )


    path.write_text(
        content,
        encoding="utf-8-sig"
    )


    if not path.exists():

        raise RuntimeError(
            "ASS file creation failed"
        )


    if path.stat().st_size <= 0:

        raise RuntimeError(
            "ASS file empty"
        )


    return str(path)



# ============================================================
# TEST
# ============================================================


if __name__ == "__main__":


    mock_segments = [

        {
            "start":0.0,
            "end":2.0,
            "text":"halo dunia",
            "words":[

                {
                    "word":"halo",
                    "start":0.0,
                    "end":0.5
                },

                {
                    "word":"dunia",
                    "start":0.5,
                    "end":1.0
                }

            ]
        }

    ]


    result = render_ass(
        mock_segments,
        "test_output.ass"
    )


    print(
        "Created:",
        result
    )