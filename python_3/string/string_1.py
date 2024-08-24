import random
import string

def generate_key(length):
    """Generate a random key of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encrypt(text, key):
    """Encrypt plaintext using a simple Caesar cipher."""
    encrypted_text = ''
    for char in text:
        if char in string.ascii_letters:
            shifted_index = (string.ascii_letters.index(char) + key) % 52
            encrypted_text += string.ascii_letters[shifted_index]
        elif char in string.digits:
            shifted_index = (string.digits.index(char) + key) % 10
            encrypted_text += string.digits[shifted_index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    """Decrypt the encrypted text."""
    return encrypt(encrypted_text, -key)

# Main program
plaintext = input("Masukkan teks yang akan dienkripsi: ")
print("Plaintext:", plaintext)

# Generate a random key
key = random.randint(1, 25)
print("Key:", key)

# Encrypt the plaintext
encrypted_text = encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

# Decrypt the encrypted text

