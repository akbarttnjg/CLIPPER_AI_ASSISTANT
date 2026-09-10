from pathlib import Path
from typing import List, Dict

def create_ass_file(output: str, events: List[Dict[str, str]]) -> Path:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = [
        "[Script Info]",
        "ScriptType: v4.00+",
        "",
        "[Events]",
        "Format: Layer, Start, End, Style, Text"
    ]
    for e in events:
        content.append(
            f"Dialogue: 0,{e['start']},{e['end']},Default,{e['text']}"
        )
    path.write_text("\n".join(content), encoding="utf-8")
    return path
