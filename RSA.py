

# Extended Euclidean Algorithm to find gcd and coefficients
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Modular inverse: find d such that (d * e) % phi == 1
def modinv(e, phi):
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise ValueError("e and phi are not coprime, modular inverse does not exist")
    return x % phi

# 1) Manually implement key generation using small primes
def generate_small_rsa_keys():
    # Choose small primes (ONLY for learning, not secure in real life)
    p = 61
    q = 53

    n = p * q                    # modulus n = p * q
    phi = (p - 1) * (q - 1)      # Euler's totient

    e = 17                       # public exponent
    # Compute private exponent d as modular inverse of e mod phi
    d = modinv(e, phi)           # private exponent

    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# 2) Encrypting a message (using public key)
def encrypt_small_rsa(message, public_key):
    e, n = public_key
    ciphertext = []
    for ch in message:
        m = ord(ch)              # character -> integer
        c = pow(m, e, n)         # c = m^e mod n
        ciphertext.append(c)
    return ciphertext

# 3) Decrypting a message (using private key)
def decrypt_small_rsa(ciphertext, private_key):
    d, n = private_key
    plaintext_chars = []
    for c in ciphertext:
        m = pow(c, d, n)         # m = c^d mod n
        plaintext_chars.append(chr(m))  # integer -> character
    return "".join(plaintext_chars)

# Test it on your name or a short string
if __name__ == "__main__":
    public_key, private_key = generate_small_rsa_keys()
    print("Public key (e, n):", public_key)
    print("Private key (d, n):", private_key)

    # You can change this to your own name
    message = "Menahil"
    print("\nOriginal message:", message)

    ciphertext = encrypt_small_rsa(message, public_key)
    print("Encrypted ciphertext (list of numbers):", ciphertext)

    decrypted_message = decrypt_small_rsa(ciphertext, private_key)
    print("Decrypted message:", decrypted_message)
