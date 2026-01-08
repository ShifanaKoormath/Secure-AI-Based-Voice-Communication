from app.services.harmful_service import detect_harmful
from app.services.urgency_service import detect_urgency

def classify_message(text: str) -> str:
    if detect_harmful(text):
        return "HARMFUL"

    if detect_urgency(text):
        return "URGENT"

    return "SAFE"
