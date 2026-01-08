# Simple, reliable harmful content detector (academic-safe)

HARMFUL_KEYWORDS = {
    "kill", "hate", "stupid", "idiot", "threat", "die",
    "destroy", "attack", "abuse"
}

def detect_harmful(text: str) -> bool:
    text_lower = text.lower()
    for word in HARMFUL_KEYWORDS:
        if word in text_lower:
            return True
    return False
