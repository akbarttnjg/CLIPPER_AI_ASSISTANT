from typing import List, Dict

def detect_hooks(transcript: List[Dict[str, float]]) -> List[Dict[str, float]]:
    return sorted(transcript, key=lambda x: x.get("score", 0), reverse=True)
