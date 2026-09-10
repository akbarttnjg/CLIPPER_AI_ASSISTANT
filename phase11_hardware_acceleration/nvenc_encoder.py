def build_nvenc_args(codec: str = "h264_nvenc") -> list[str]:
    return ["-c:v", codec, "-preset", "p5"]
