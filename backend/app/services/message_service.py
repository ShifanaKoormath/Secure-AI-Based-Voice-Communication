import base64
import uuid
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STORAGE_AUDIO = BASE_DIR / "storage" / "encrypted_audio"
STORAGE_META = BASE_DIR / "storage" / "metadata"


def save_message(sender: str, nonce: bytes, ciphertext: bytes, aes_key: bytes):
    message_id = str(uuid.uuid4())

    # Save encrypted audio
    audio_path = STORAGE_AUDIO / f"{message_id}.bin"
    with open(audio_path, "wb") as f:
        f.write(nonce + ciphertext)

    # Save metadata + AES key (base64)
    metadata = {
        "message_id": message_id,
        "sender": sender,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "PENDING",
        "aes_key": base64.b64encode(aes_key).decode()
    }

    meta_path = STORAGE_META / f"{message_id}.json"
    with open(meta_path, "w") as f:
        json.dump(metadata, f)

    return metadata



def list_messages():
    messages = []
    for meta_file in STORAGE_META.glob("*.json"):
        with open(meta_file, "r") as f:
            messages.append(json.load(f))
    return messages
