from clipper_ai.config import settings, Settings


def test_settings_export():
    assert isinstance(settings, Settings)
    assert settings.project_name == "CLIPPER_AI_ASSISTANT"
