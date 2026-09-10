# FINAL FIX v4

Fixes from v3:
- Added VERSION export in clipper_ai.__init__
- Added clipper_ai.mcp.server.create_server
- Simplified setuptools package discovery
- Removed ambiguous root package discovery

Install:
pip uninstall clipper-ai-assistant -y
pip install -e .
pytest
