from phase30_release.environment_checker.checker import check_environment

def test_release_environment():
    result = check_environment()
    assert result["python"] is True
