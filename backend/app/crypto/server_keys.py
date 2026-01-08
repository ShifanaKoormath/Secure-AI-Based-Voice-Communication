from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization
from pathlib import Path

# Persistent server key file
KEY_FILE = Path("storage/server_private.key")


def load_or_create_server_key():
    if KEY_FILE.exists():
        private_bytes = KEY_FILE.read_bytes()
        private_key = x25519.X25519PrivateKey.from_private_bytes(private_bytes)
    else:
        private_key = x25519.X25519PrivateKey.generate()
        KEY_FILE.parent.mkdir(parents=True, exist_ok=True)
        KEY_FILE.write_bytes(
            private_key.private_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PrivateFormat.Raw,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    return private_key, private_key.public_key()
