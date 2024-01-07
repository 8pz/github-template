import base64, wmi
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

def fetch_key():
    c = wmi.WMI()
    for board in c.Win32_BaseBoard():
        device_identifier = str(board.SerialNumber.strip()).encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=device_identifier,
        length=32,
        backend=default_backend()
    )

    key = kdf.derive(device_identifier)

    key = base64.urlsafe_b64encode(key)
    return key

def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data

