def test_phase26_30_imports():
    import phase30_release
    from phase30_release.environment_checker.checker import check_environment

    result = check_environment()

    assert isinstance(result, dict)
    assert result["python"] is True
