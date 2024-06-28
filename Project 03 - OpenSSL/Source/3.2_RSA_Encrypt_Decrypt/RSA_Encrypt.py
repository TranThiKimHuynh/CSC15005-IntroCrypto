import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def encrypt_with_rsa_public_key_pem(rsa_public_key_pem, plaintext):
    # Convert public key RSA from PEM
    rsa_public_key = serialization.load_pem_public_key(
        rsa_public_key_pem.encode(),
        backend=default_backend()
    )

    # Encrypt message using public key and RSA padding PKCS#1 v1.5
    ciphertext = rsa_public_key.encrypt(
        plaintext.encode(),
        padding.PKCS1v15()
    )

    return ciphertext

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)



if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py must have <public_key_path> <plaintex_file_path> <cipher_file_path>")
        sys.exit(1)
     # Extract file paths from command-line arguments
    public_key_path = sys.argv[1]
    plaintext_file_path = sys.argv[2]
    ciphertext_file_path = sys.argv[3]
    
    # Using public key RSA from file path
    with open(public_key_path, 'rb') as f:
        rsa_public_key_pem = f.read().decode()
    # Read data from plaintext_file_path 
    plaintext = read_file(plaintext_file_path)

    # Decrypt using private key and RSA padding PKCS#1 v1.5
    ciphertext_python = encrypt_with_rsa_public_key_pem(rsa_public_key_pem, plaintext)

    # Write result to file ciphertext_file_path
    write_to_file(ciphertext_file_path, ciphertext_python)
    print("Encryption complete.")
