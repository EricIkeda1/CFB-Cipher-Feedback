from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Defina uma chave fixa (32 bytes para AES-256)
key = b'\x01' * 32  
iv = b'\x01' * 16  

# Função para cifrar o texto simples usando o modo CFB
def encrypt(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

# Função para decifrar o texto cifrado usando o modo CFB
def decrypt(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_text

# Função principal
def main():
    global iv  

    # Menu de opções
    choice = input("Digite 1 para cifrar ou 2 para decifrar: ")

    if choice == '1':
        # Solicitar ao usuário que digite o texto simples
        plaintext = input("Digite o texto simples: ").encode()

        # Cifrar
        ciphertext = encrypt(key, iv, plaintext)
        print(f"Cifrado: {ciphertext.hex()}")
        print(f"IV: {iv.hex()}") 

    elif choice == '2':
        # Solicitar ao usuário que digite o texto cifrado e o IV
        ciphertext_input = input("Digite o texto cifrado em hexadecimal: ")
        iv_input = input("Digite o IV em hexadecimal: ")
        ciphertext = bytes.fromhex(ciphertext_input)
        iv = bytes.fromhex(iv_input)  

        # Decifrar
        decrypted_text = decrypt(key, iv, ciphertext)
        print(f"Decifrado: {decrypted_text.decode()}")

    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")

if __name__ == "__main__":
    main()
