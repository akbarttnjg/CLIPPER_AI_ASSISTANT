# Phase 3.2.1 Pipeline Orchestrator Engine

Purpose:
Connect MCP tool execution into a deterministic media processing workflow.

Implemented:
- Pipeline job model
- Stage registration
- Sequential execution engine
- Metadata tracking

Pipeline flow foundation:

Claude
 -> MCP
 -> Tool Executor
 -> Pipeline Orchestrator
 -> FFmpeg / Whisper / Subtitle / FCPXML
