
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generate_rsa_keypair(bits=2048):

    private_key = RSA.generate(bits)
    public_key = private_key.publickey()
    return private_key, public_key


def encrypt_with_pycryptodome(message, public_key):

    cipher = PKCS1_OAEP.new(public_key)        # use OAEP padding
    ciphertext = cipher.encrypt(message.encode("utf-8"))
    return ciphertext


def decrypt_with_pycryptodome(ciphertext, private_key):

    cipher = PKCS1_OAEP.new(private_key)
    plaintext_bytes = cipher.decrypt(ciphertext)
    return plaintext_bytes.decode("utf-8")


if __name__ == "__main__":

    private_key, public_key = generate_rsa_keypair(bits=2048)
    print("Generated 2048-bit RSA key pair.")


    message = input("Enter a message to encrypt for Task 2: ")
    print("Original message:", message)


    ciphertext = encrypt_with_pycryptodome(message, public_key)


    ciphertext_hex = binascii.hexlify(ciphertext).decode("utf-8")
    print("Ciphertext (hex):", ciphertext_hex)


    decrypted_message = decrypt_with_pycryptodome(ciphertext, private_key)
    print("Decrypted message:", decrypted_message)