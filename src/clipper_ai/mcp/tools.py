from typing import Dict, Any, Callable

from clipper_ai.media.ffmpeg_engine import cut_video
from clipper_ai.media.whisper_engine import (
    transcribe_video,
    transcribe_audio,
)
from clipper_ai.subtitle.renderer import create_ass_file
from clipper_ai.davinci.fcpxml_generator import create_fcpxml


TOOLS: Dict[str, Dict[str, Any]] = {

    "cut_video": {

        "handler": cut_video,

        "schema": {

            "type": "object",

            "properties": {

                "source": {
                    "type": "string"
                },

                "output": {
                    "type": "string"
                },

                "start": {
                    "type": "string"
                },

                "end": {
                    "type": "string"
                },

            },

            "required": [
                "source",
                "output",
                "start",
                "end",
            ],

        },

    },


    "transcribe_audio": {

        "handler": transcribe_audio,

        "schema": {

            "type": "object",

            "properties": {

                "audio": {
                    "type": "string"
                },

                "model": {
                    "type": "string"
                },

                "device": {
                    "type": "string"
                },

            },

            "required": [
                "audio"
            ],

        },

    },


    "transcribe_video": {

        "handler": transcribe_video,

        "schema": {

            "type": "object",

            "properties": {

                "video": {
                    "type": "string"
                },

                "model": {
                    "type": "string"
                },

                "device": {
                    "type": "string"
                },

            },

            "required": [
                "video"
            ],

        },

    },


    "generate_subtitle": {

        "handler": create_ass_file,

        "schema": {

            "type": "object",

            "properties": {

                "output": {
                    "type": "string"
                },

                "events": {
                    "type": "array"
                },

            },

            "required": [
                "output",
                "events"
            ],

        },

    },


    "export_fcpxml": {

        "handler": create_fcpxml,

        "schema": {

            "type": "object",

            "properties": {

                "output": {
                    "type": "string"
                },

                "clips": {
                    "type": "array"
                },

            },

            "required": [
                "output",
                "clips"
            ],

        },

    },

}



def get_tool_registry():
    return TOOLS