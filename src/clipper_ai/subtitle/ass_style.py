"""
Advanced SubStation Alpha (ASS) style engine.

Responsibilities:
- Define subtitle visual styles
- Convert RGB colors to ASS BGR format
- Generate ASS style headers
- Provide TikTok/Reels caption presets
- Convert timestamps into ASS format
"""


from __future__ import annotations


from dataclasses import dataclass
from typing import Tuple


RGBColor = Tuple[int, int, int]



@dataclass(frozen=True)
class ASSStyle:
    """
    Represents one ASS subtitle style.

    Designed for professional short-form video captions.

    ASS color format internally:
        &HBBGGRR&

    """

    name: str = "Viral"


    font_name: str = "Arial"


    font_size: int = 80


    primary_color: RGBColor = (
        255,
        255,
        255,
    )


    secondary_color: RGBColor = (
        255,
        255,
        0,
    )


    outline_color: RGBColor = (
        0,
        0,
        0,
    )


    back_color: RGBColor = (
        0,
        0,
        0,
    )


    bold: bool = True


    italic: bool = False


    underline: bool = False


    strikeout: bool = False


    scale_x: int = 100


    scale_y: int = 100


    spacing: int = 0


    angle: int = 0


    border_style: int = 1


    outline: int = 5


    shadow: int = 2


    alignment: int = 2


    margin_l: int = 60


    margin_r: int = 60


    margin_v: int = 350



def validate_rgb(
    color: RGBColor,
) -> None:
    """
    Validate RGB color range.

    Args:
        color:
            Tuple containing R,G,B values.

    Raises:
        ValueError:
            Invalid RGB value.
    """


    if len(color) != 3:

        raise ValueError(
            "RGB color requires 3 values"
        )


    for channel in color:

        if not isinstance(
            channel,
            int,
        ):

            raise ValueError(
                "RGB values must be integers"
            )


        if channel < 0 or channel > 255:

            raise ValueError(
                f"RGB channel out of range: {channel}"
            )



def rgb_to_ass(
    color: RGBColor,
) -> str:
    """
    Convert RGB tuple to ASS color.

    ASS uses:

        &HBBGGRR&

    Example:

        RGB:
            (255,255,0)

        Output:
            &H00FFFF&

    """


    validate_rgb(color)


    r, g, b = color


    return (
        f"&H"
        f"{b:02X}"
        f"{g:02X}"
        f"{r:02X}"
        f"&"
    )



def bool_to_ass(
    value: bool,
) -> int:
    """
    Convert boolean to ASS flag.

    ASS:
        enabled = -1
        disabled = 0
    """


    return -1 if value else 0



def seconds_to_ass_timestamp(
    seconds: float,
) -> str:
    """
    Convert seconds into ASS timestamp.

    Format:

        H:MM:SS.cc

    Example:

        65.25

    becomes:

        0:01:05.25
    """


    if seconds < 0:

        raise ValueError(
            "Timestamp cannot be negative"
        )


    hours = int(
        seconds // 3600
    )


    minutes = int(
        (seconds % 3600)
        //
        60
    )


    remaining = (
        seconds
        %
        60
    )


    whole_seconds = int(
        remaining
    )


    centiseconds = int(
        round(
            (
                remaining
                -
                whole_seconds
            )
            *
            100
        )
    )


    if centiseconds >= 100:

        whole_seconds += 1
        centiseconds = 0


    return (
        f"{hours}:"
        f"{minutes:02d}:"
        f"{whole_seconds:02d}."
        f"{centiseconds:02d}"
    )



def generate_ass_style_line(
    style: ASSStyle,
) -> str:
    """
    Generate ASS Style line.

    Compatible with:

        [V4+ Styles]

    """


    return (
        "Style: "
        f"{style.name},"
        f"{style.font_name},"
        f"{style.font_size},"
        f"{rgb_to_ass(style.primary_color)},"
        f"{rgb_to_ass(style.secondary_color)},"
        f"{rgb_to_ass(style.outline_color)},"
        f"{rgb_to_ass(style.back_color)},"
        f"{bool_to_ass(style.bold)},"
        f"{bool_to_ass(style.italic)},"
        f"{bool_to_ass(style.underline)},"
        f"{bool_to_ass(style.strikeout)},"
        f"{style.scale_x},"
        f"{style.scale_y},"
        f"{style.spacing},"
        f"{style.angle},"
        f"{style.border_style},"
        f"{style.outline},"
        f"{style.shadow},"
        f"{style.alignment},"
        f"{style.margin_l},"
        f"{style.margin_r},"
        f"{style.margin_v}"
    )



def generate_ass_header(
    style: ASSStyle,
    width: int = 1080,
    height: int = 1920,
) -> str:
    """
    Generate complete ASS subtitle header.

    Default:
        TikTok/Reels vertical format.

    """


    return f"""
[Script Info]
Title: CLIPPER AI Subtitle
ScriptType: v4.00+
WrapStyle: 2
ScaledBorderAndShadow: yes
PlayResX: {width}
PlayResY: {height}


[V4+ Styles]
Format:
Name,
Fontname,
Fontsize,
PrimaryColour,
SecondaryColour,
OutlineColour,
BackColour,
Bold,
Italic,
Underline,
StrikeOut,
ScaleX,
ScaleY,
Spacing,
Angle,
BorderStyle,
Outline,
Shadow,
Alignment,
MarginL,
MarginR,
MarginV


{generate_ass_style_line(style)}


[Events]
Format:
Layer,
Start,
End,
Style,
Text

""".strip()



def create_tiktok_style() -> ASSStyle:
    """
    Create professional TikTok/Reels caption preset.

    Visual:

    Normal:
        White text

    Highlight:
        Yellow text

    Outline:
        Black thick border

    Position:
        Bottom center
    """


    return ASSStyle(
        name="TikTokViral",

        font_name="Arial",

        font_size=80,


        primary_color=(
            255,
            255,
            255,
        ),


        secondary_color=(
            255,
            255,
            0,
        ),


        outline_color=(
            0,
            0,
            0,
        ),


        back_color=(
            0,
            0,
            0,
        ),


        bold=True,


        outline=5,

        shadow=2,


        alignment=2,


        margin_l=60,

        margin_r=60,

        margin_v=350,
    )