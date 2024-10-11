from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def generate_key_iv():
    key = os.urandom(16)  
    iv = os.urandom(16)   
    return key, iv

def encrypt(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

if __name__ == "__main__":
    key, iv = generate_key_iv()
    data = b"ATACARBASENORTE"  

    print("Texto original:", data.decode())
    ciphertext = encrypt(data, key, iv)
    print("Texto cifrado:", ciphertext.hex())
    decrypted_data = decrypt(ciphertext, key, iv)
    print("Texto decifrado:", decrypted_data.decode())
