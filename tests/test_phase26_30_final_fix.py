def test_phase30_package_import():
    from phase30_release.environment_checker.checker import check_environment

    result = check_environment()

    assert isinstance(result, dict)
    assert result["python_available"] is True


def test_phase_packages_exist():
    import phase26_claude_mcp_bridge
    import phase27_video_director
    import phase28_autonomous_pipeline
    import phase29_cluster_render
    import phase30_release
