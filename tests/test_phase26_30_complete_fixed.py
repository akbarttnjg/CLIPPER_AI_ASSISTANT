def test_phase30_import():
    from phase30_release.environment_checker.checker import check_environment
    result = check_environment()
    assert result["python"] is True
