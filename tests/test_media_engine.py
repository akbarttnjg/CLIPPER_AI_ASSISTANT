from pathlib import Path
from clipper_ai.media.subtitle_renderer import create_ass_file


def test_ass_creation(tmp_path):
    output = tmp_path / "test.ass"

    result = create_ass_file(
        str(output),
        [
            {
                "start": "0:00:00.00",
                "end": "0:00:02.00",
                "text": "Hello"
            }
        ],
    )

    assert result.exists()
