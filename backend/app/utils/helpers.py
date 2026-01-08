import base64
import json
from pathlib import Path
from app.crypto.aes import decrypt_audio

def load_and_decrypt_audio(encrypted_path: Path, meta_path: Path) -> bytes:
    data = encrypted_path.read_bytes()
    nonce = data[:12]
    ciphertext = data[12:]

    meta = json.loads(meta_path.read_text())
    aes_key = base64.b64decode(meta["aes_key"])

    return decrypt_audio(aes_key, nonce, ciphertext)
