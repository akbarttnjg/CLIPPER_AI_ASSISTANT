from dataclasses import dataclass
import shutil

@dataclass
class HardwareInfo:
    ffmpeg: bool
    cuda_available: bool

def probe_hardware() -> HardwareInfo:
    return HardwareInfo(
        ffmpeg=shutil.which("ffmpeg") is not None,
        cuda_available=False
    )
