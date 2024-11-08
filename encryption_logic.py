import os


def xor_bytes(data, key):
    """Simple XOR-based encryption/decryption."""
    key_repeated = (key * (len(data) // len(key) + 1))[:len(data)]
    return bytes([b ^ k for b, k in zip(data, key_repeated)])


def des_encrypt(plaintext, des_key):
    plaintext_bytes = plaintext.encode()
    return xor_bytes(plaintext_bytes, des_key)


def des_decrypt(ciphertext, des_key):
    return xor_bytes(ciphertext, des_key).decode()


def aes_encrypt(data, aes_key):
    return xor_bytes(data, aes_key)


def aes_decrypt(data, aes_key):
    return xor_bytes(data, aes_key)


# Generate random keys for DES and AES
DES_KEY = os.urandom(8)  # 8-byte key for DES
AES_KEY = os.urandom(16)  # 16-byte key for AES
