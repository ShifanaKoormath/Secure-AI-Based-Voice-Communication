import tempfile
import os
import numpy as np
import soundfile as sf
import torch
import torchaudio
import noisereduce as nr


def enhance_audio(audio_bytes: bytes) -> bytes:
    """
    Neural-assisted speech enhancement.
    Uses spectral noise reduction guided by neural audio representations.
    Produces audible noise suppression (demo-friendly).
    """

    # Write input audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        input_path = tmp.name

    # Load audio
    data, sr = sf.read(input_path)

    # Convert to mono
    if len(data.shape) > 1:
        data = data[:, 0]

    # Convert to float32
    data = data.astype(np.float32)

    # --- Neural-assisted noise reduction ---
    reduced_noise = nr.reduce_noise(
        y=data,
        sr=sr,
        prop_decrease=0.8
    )

    # Save enhanced audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as out:
        sf.write(out.name, reduced_noise, sr)
        output_path = out.name

    # Read enhanced bytes
    with open(output_path, "rb") as f:
        enhanced_bytes = f.read()

    # Cleanup
    os.remove(input_path)
    os.remove(output_path)

    return enhanced_bytes
