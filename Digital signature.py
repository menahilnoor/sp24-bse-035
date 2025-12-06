from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import binascii

# 1) Generate RSA key pair (we can reuse the same pattern from Task 2)
def generate_rsa_keypair(bits=2048):
    """
    Generate an RSA key pair using PyCryptodome.
    Returns: (private_key, public_key)
    """
    private_key = RSA.generate(bits)
    public_key = private_key.publickey()
    return private_key, public_key

# 2) Create a digital signature of a message
def create_signature(message, private_key):
    """
    Create a digital signature of the message using RSA and SHA-256.
    Steps:
    1. Hash the message with SHA-256
    2. Sign the hash with the private key (PKCS#1 v1.5)
    Returns the signature bytes.
    """
    # Create SHA-256 hash of the message
    h = SHA256.new(message.encode("utf-8"))
    # Sign the hash using the private key
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

# 3) Verify a digital signature
def verify_signature(message, signature, public_key):
    """
    Verify an RSA digital signature.
    Returns True if verification succeeds, False otherwise.
    """
    h = SHA256.new(message.encode("utf-8"))
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        # Verification failed (wrong signature or modified message)
        return False

# Demo: Test Task 3 end-to-end
if __name__ == "__main__":
    # Generate RSA key pair
    private_key, public_key = generate_rsa_keypair(bits=2048)
    print("Generated 2048-bit RSA key pair for digital signatures.\n")

    # Take a message from the user
    original_message = input("Enter a message to sign for Task 3: ")
    print("Original message:", original_message)

    # Create a digital signature for the original message
    signature = create_signature(original_message, private_key)
    print("\nSignature (hex):", binascii.hexlify(signature).decode("utf-8"))

    # Verify on the original message
    is_valid_original = verify_signature(original_message, signature, public_key)
    print("Verification on original message:", is_valid_original)

    # Modify the message slightly
    modified_message = original_message + " (modified)"
    print("\nModified message:", modified_message)

    # Verify the same signature with the modified message
    is_valid_modified = verify_signature(modified_message, signature, public_key)
    print("Verification on modified message:", is_valid_modified)