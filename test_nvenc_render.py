from pathlib import Path

from src.clipper_ai.video.ffmpeg_renderer import (
    render_with_ass_nvenc
)


VIDEO = (
    r"C:\Users\ASUS\Downloads\YTDown.com_YouTube_Take-Profit-Show-Cara-Gaji-UMR-Dapat-1-M_Media_cCrFMckqS0M_001_1080p_cut.mp4"
)


ASS = (
    r"C:\CLIPPER_AI_ASSISTANT\src\clipper_ai\subtitle\test_output.ass"
)


OUTPUT = (
    r"C:\CLIPPER_AI_ASSISTANT\test_nvenc_output.mp4"
)



if __name__ == "__main__":


    result = render_with_ass_nvenc(
        input_video=VIDEO,
        subtitle_file=ASS,
        output_video=OUTPUT,
    )


    print(
        "DONE:",
        result
    )