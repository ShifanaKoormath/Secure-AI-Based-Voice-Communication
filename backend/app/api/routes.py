from fastapi import APIRouter, UploadFile, File, Form
from pathlib import Path
import json
from fastapi.responses import FileResponse
import tempfile
import soundfile as sf
import os

from app.services.enhancement_service import enhance_audio

from app.crypto.key_exchange import derive_shared_secret, generate_keypair
from app.crypto.aes import derive_aes_key, encrypt_audio
from app.crypto.server_keys import load_or_create_server_key

from app.services.message_service import (
    save_message,
    list_messages,
    STORAGE_AUDIO,
    STORAGE_META,
)

from app.utils.helpers import load_and_decrypt_audio
from app.services.stt_service import speech_to_text
from app.services.classify_service import classify_message

router = APIRouter(prefix="/api")

# 🔐 Persistent server key (CRITICAL)
SERVER_PRIVATE_KEY, SERVER_PUBLIC_KEY = load_or_create_server_key()


# -----------------------------
# Upload & Encrypt Voice
# -----------------------------
@router.post("/send-voice")
async def send_voice(
    sender: str = Form(...),
    audio: UploadFile = File(...)
):
    # Read audio bytes
    audio_bytes = await audio.read()

    # 🔑 Simulated client keypair (demo-safe)
    client_private, client_public = generate_keypair()

    # 🔐 Shared secret
    shared_secret = derive_shared_secret(
        SERVER_PRIVATE_KEY, client_public
    )

    # 🔒 AES key
    aes_key = derive_aes_key(shared_secret)

    # 🔐 Encrypt audio
    nonce, ciphertext = encrypt_audio(aes_key, audio_bytes)

    # 📦 Store encrypted message
    metadata = save_message(
        sender=sender,
        nonce=nonce,
        ciphertext=ciphertext,
        aes_key=aes_key
    )

    return {
        "message": "Voice message stored securely",
        "metadata": metadata
    }


# -----------------------------
# List Messages (Inbox)
# -----------------------------
@router.get("/messages")
def get_messages():
    return list_messages()

# -----------------------------
# DEMO: Get Enhanced Audio
# -----------------------------
@router.get("/enhance/{message_id}")
def get_enhanced_audio(message_id: str):
    encrypted_path = STORAGE_AUDIO / f"{message_id}.bin"
    meta_path = STORAGE_META / f"{message_id}.json"

    if not encrypted_path.exists() or not meta_path.exists():
        return {"error": "Message not found"}

    # 🔓 Decrypt audio
    audio_bytes = load_and_decrypt_audio(
        encrypted_path,
        meta_path
    )

    # 🎧 Enhance audio (Objective 2)
    enhanced_audio = enhance_audio(audio_bytes)

    # Save enhanced audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(enhanced_audio)
        temp_path = tmp.name

    # Return audio file
    return FileResponse(
        path=temp_path,
        media_type="audio/wav",
        filename=f"{message_id}_enhanced.wav"
    )

# -----------------------------
# Decrypt → Enhance → Transcribe → Classify
# -----------------------------
@router.get("/transcribe/{message_id}")
def transcribe_message(message_id: str):
    encrypted_path = STORAGE_AUDIO / f"{message_id}.bin"
    meta_path = STORAGE_META / f"{message_id}.json"

    if not encrypted_path.exists() or not meta_path.exists():
        return {"error": "Message not found"}

    # 🔓 Step 1: Decrypt audio (controlled)
    audio_bytes = load_and_decrypt_audio(
        encrypted_path,
        meta_path
    )

    # 🎧 Step 2: Speech enhancement (Objective 2)
    enhanced_audio = enhance_audio(audio_bytes)

    # 🧠 Step 3: Speech-to-text
    transcription = speech_to_text(enhanced_audio)

    # 🧠 Step 4: NLP classification
    status = classify_message(transcription)

    # 🔄 Update metadata
    meta = json.loads(meta_path.read_text())
    meta["status"] = status
    meta_path.write_text(json.dumps(meta, indent=2))

    return {
        "message_id": message_id,
        "transcription": transcription,
        "status": status
    }
