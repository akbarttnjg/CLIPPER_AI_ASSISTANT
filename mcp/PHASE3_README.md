# Phase 3 — Claude Code MCP Bridge

Status:
Prepared for real Claude Code integration.

Flow:

Claude Code
    |
    v
MCP Configuration
    |
    v
clipper_ai.mcp.launcher
    |
    +-- Tool Registry
    +-- FFmpeg Pipeline
    +-- Whisper CUDA Engine
    +-- Subtitle Renderer
    +-- DaVinci FCPXML Bridge

Installation:

1. Copy claude_mcp_config.example.json into Claude MCP configuration.
2. Adjust Python path if required.
3. Restart Claude Code.
4. Test MCP server discovery.

Next expansion:
Phase 3.1 Real Tool Invocation.
