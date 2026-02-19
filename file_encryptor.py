
"""
File encryption and decryption module for Advanced Cybersecurity Tool.
Uses Fernet symmetric encryption from the cryptography library.
"""

from cryptography.fernet import Fernet
import base64
import os

def encrypt_file(filename, key):
    """
    Encrypt a file using the provided key.
    Args:
        filename (str): Path to the file to encrypt.
        key (str): Encryption key (32 bytes or Fernet key).
    """
    try:
        fernet = Fernet(_format_key(key))
        with open(filename, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(filename + '.enc', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        print(f"File encrypted: {filename}.enc")
    except Exception as e:
        print(f"Encryption failed: {e}")

def decrypt_file(filename, key):
    """
    Decrypt a file using the provided key.
    Args:
        filename (str): Path to the file to decrypt.
        key (str): Decryption key (32 bytes or Fernet key).
    """
    try:
        fernet = Fernet(_format_key(key))
        with open(filename, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        out_file = filename.replace('.enc', '.dec')
        with open(out_file, 'wb') as dec_file:
            dec_file.write(decrypted)
        print(f"File decrypted: {out_file}")
    except Exception as e:
        print(f"Decryption failed: {e}")

def _format_key(key):
    """
    Format the key to be valid for Fernet (32 url-safe base64-encoded bytes).
    Args:
        key (str): User-provided key.
    Returns:
        bytes: Fernet-compatible key.
    Raises:
        ValueError: If the key is not valid.
    """
    try:
        key_bytes = key.encode()
        if len(key_bytes) == 32:
            return base64.urlsafe_b64encode(key_bytes)
        elif len(key_bytes) == 44:
            return key_bytes
        else:
            raise ValueError("Key must be 32 bytes or a valid Fernet key.")
    except Exception as e:
        raise ValueError(f"Invalid key: {e}")
