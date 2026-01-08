from transformers import pipeline

# Lightweight BERT-based urgency classifier
urgency_classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

URGENT_KEYWORDS = {
    "urgent", "immediately", "asap", "help", "emergency", "now"
}

def detect_urgency(text: str) -> bool:
    text_lower = text.lower()
    for word in URGENT_KEYWORDS:
        if word in text_lower:
            return True

    # Optional sentiment-based signal
    result = urgency_classifier(text)[0]
    if result["label"] == "NEGATIVE" and result["score"] > 0.9:
        return True

    return False
