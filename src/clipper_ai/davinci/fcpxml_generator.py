from pathlib import Path

def create_fcpxml(output: str, clips: list[str]) -> Path:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    xml = "<?xml version='1.0'?><fcpxml><resources></resources><library/></fcpxml>"
    path.write_text(xml, encoding="utf-8")
    return path
