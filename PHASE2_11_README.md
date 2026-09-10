# Phase 2.11 — MCP Tool Schema Documentation

Purpose:
Provide machine-readable documentation for Claude Code MCP tool usage.

Available schemas:

- cut_video.schema.json
- whisper.schema.json
- subtitle.schema.json
- davinci.schema.json

Flow:

Claude Code
    |
    v
MCP Tool Schema
    |
    v
CLIPPER_AI_ASSISTANT MCP Server
    |
    +-- FFmpeg
    +-- Whisper CUDA
    +-- ASS Subtitle
    +-- DaVinci FCPXML

This phase prepares the system for Phase 3 real Claude tool invocation.
