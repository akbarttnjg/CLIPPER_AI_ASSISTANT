from clipper_ai.subtitle.word_timing import WordTimingProcessor


mock = {
    "segments": [
        {
            "words": [
                {
                    "word":"halo",
                    "start":0.0,
                    "end":0.5
                },
                {
                    "word":"dunia",
                    "start":0.5,
                    "end":1.0
                },
                {
                    "word":"ini",
                    "start":1.0,
                    "end":1.3
                },
            ]
        }
    ]
}


processor = WordTimingProcessor(
    max_words=2
)


words = processor.flatten_words(mock)

chunks = processor.create_chunks(words)


print(words)
print(chunks)