import whisper
import tempfile
import os

model = whisper.load_model("base")

def speech_to_text(audio_bytes: bytes) -> str:
    tmp = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )
    try:
        tmp.write(audio_bytes)
        tmp.close()  # 🔑 CRITICAL FOR WINDOWS

        result = model.transcribe(tmp.name)
        return result["text"]
    finally:
        os.unlink(tmp.name)  # cleanup
	
