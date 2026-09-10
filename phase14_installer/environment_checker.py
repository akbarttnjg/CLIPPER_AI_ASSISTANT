import shutil

def check_dependencies() -> dict:
    return {"ffmpeg": shutil.which("ffmpeg") is not None}
