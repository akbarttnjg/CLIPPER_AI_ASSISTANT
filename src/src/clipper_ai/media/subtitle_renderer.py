from pathlib import Path
from typing import List, Dict


def ass_time(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centis = int((seconds - int(seconds)) * 100)
    return f"{hours}:{minutes:02}:{secs:02}.{centis:02}"


def create_ass_file(
    output: str,
    events: List[Dict[str, str]],
) -> Path:
    """Create Advanced SubStation Alpha subtitle file."""

    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "[Script Info]",
        "ScriptType: v4.00+",
        "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour",
        "Style: Default,Arial,48,&H00FFFFFF",
        "",
        "[Events]",
        "Format: Layer, Start, End, Style, Text",
    ]

    for item in events:
        lines.append(
            f"Dialogue: 0,{item['start']},{item['end']},Default,{item['text']}"
        )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if not path.exists() or path.stat().st_size == 0:
        raise RuntimeError("ASS file invalid")

    return path
