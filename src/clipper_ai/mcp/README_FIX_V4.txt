CLIPPER_AI_ASSISTANT_MCP_FIX_v4

Purpose:
Fix Claude Code showing:
connected · no tools

Cause:
MCP SDK 2.x migration changed server API.
The old FastMCP import path was invalid.

This patch exposes:
- tools/list
- tools/call

Expected Claude result:
clipper-ai-assistant connected · tools available
