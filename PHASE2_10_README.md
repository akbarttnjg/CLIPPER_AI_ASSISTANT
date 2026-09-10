# Phase 2.10 — MCP Manifest + Claude Configuration

Purpose:
Connect Claude Code to the local CLIPPER_AI_ASSISTANT MCP server.

Flow:

Claude Code
    |
    v
MCP Manifest
    |
    v
CLIPPER_AI_ASSISTANT MCP Server
    |
    +-- FFmpeg Engine
    +-- Whisper CUDA Engine
    +-- Subtitle Engine
    +-- DaVinci Bridge

Next step:
Configure Claude Code to load the MCP server entry.
