"""Subtitle and FCPXML export foundation."""
from pathlib import Path


def export_subtitle(path: Path, content: str) -> Path:
    path.write_text(content, encoding="utf-8")
    return path


def export_fcpxml(path: Path, xml: str) -> Path:
    path.write_text(xml, encoding="utf-8")
    return path
