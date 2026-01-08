from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization


def generate_keypair():
    private_key = x25519.X25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key


def serialize_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )


def load_public_key(public_bytes):
    return x25519.X25519PublicKey.from_public_bytes(public_bytes)


def derive_shared_secret(private_key, peer_public_key):
    return private_key.exchange(peer_public_key)
