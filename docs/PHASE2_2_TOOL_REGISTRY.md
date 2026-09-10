# Phase 2.2 MCP Tool Registry

Tujuan:
Membuat daftar kemampuan CLIPPER_AI_ASSISTANT yang dapat dibaca Claude melalui MCP.

Tool saat ini:

- system_check
- video_info
- cut_video
- create_subtitle
- create_davinci_timeline

Status:
system_check aktif.
Tool produksi lainnya disiapkan untuk implementasi berikutnya.

Arsitektur:

Claude Code
    |
    MCP
    |
CLIPPER_AI_ASSISTANT
    |
Tool Registry
    |
FFmpeg / Whisper / DaVinci Bridge
