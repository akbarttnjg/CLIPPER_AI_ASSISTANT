"""
Word timing processor.

Transforms Faster Whisper output
into subtitle-ready timing structures.
"""


from __future__ import annotations

from typing import Any, Dict, List


class WordTimingProcessor:
    """
    Process Whisper word timestamps.

    Responsibilities:
    - flatten segments
    - normalize words
    - create subtitle chunks
    """


    def __init__(
        self,
        max_words: int = 5,
        max_duration: float = 3.5,
    ) -> None:

        self.max_words = max_words
        self.max_duration = max_duration



    def flatten_words(
        self,
        transcription: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        """
        Convert Whisper segments into word list.
        """

        words: List[Dict[str, Any]] = []


        index: int = 0


        for segment in transcription.get(
            "segments",
            []
        ):

            for word in segment.get(
                "words",
                []
            ):

                words.append(
                    {
                        "index": index,
                        "text": word["word"].strip(),
                        "start": float(
                            word["start"]
                        ),
                        "end": float(
                            word["end"]
                        ),
                    }
                )

                index += 1


        return words



    def create_chunks(
        self,
        words: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        Group words into subtitle chunks.
        """


        chunks: List[
            Dict[str, Any]
        ] = []


        current: List[
            Dict[str, Any]
        ] = []


        chunk_start: float = 0.0


        for word in words:


            if not current:

                chunk_start = word["start"]


            current.append(word)


            duration = (
                word["end"]
                -
                chunk_start
            )


            if (
                len(current)
                >= self.max_words
                or duration >= self.max_duration
            ):

                chunks.append(
                    self._build_chunk(
                        current
                    )
                )

                current = []


        if current:

            chunks.append(
                self._build_chunk(
                    current
                )
            )


        return chunks



    def _build_chunk(
        self,
        words: List[Dict[str, Any]],
    ) -> Dict[str, Any]:

        return {

            "start": words[0]["start"],

            "end": words[-1]["end"],

            "text": " ".join(
                item["text"]
                for item in words
            ),

            "words": words,

        }