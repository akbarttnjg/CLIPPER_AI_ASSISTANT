from clipper_ai.subtitle.ass_style import (
    ASSStyle,
    rgb_to_ass,
    seconds_to_ass_timestamp,
    generate_ass_header,
)


style = ASSStyle()


print(
    rgb_to_ass(
        (255,255,0)
    )
)


print(
    seconds_to_ass_timestamp(
        65.25
    )
)


print(
    generate_ass_header(
        style
    )
)