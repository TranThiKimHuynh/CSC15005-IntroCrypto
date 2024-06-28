import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding

def decrypt_with_rsa_private_key_pem(rsa_private_key_pem, ciphertext):
    # Convert private key RSA from PEM
    rsa_private_key = serialization.load_pem_private_key(
        rsa_private_key_pem.encode(),
        password=None,
        backend=default_backend()
    )

    # Decrypt using private key and RSA padding PKCS#1 v1.5
    plaintext = rsa_private_key.decrypt(
        ciphertext,
        asymmetric_padding.PKCS1v15()
    ).decode()

    return plaintext

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_to_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data.encode())  # Encode the string to bytes before writing

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py must have <privte_key_file_path> <ciphertext_file_path> <decryptedtext_file_path>")
        sys.exit(1)

    # Extract file paths from command-line arguments
    private_key_file_path = sys.argv[1]
    ciphertext_file_path = sys.argv[2]
    decryptedtext_file_path = sys.argv[3]

    # Read the private key from the file
    with open(private_key_file_path, 'rb') as f:
        rsa_private_key_pem = f.read().decode()

    # Read ciphertext from the file
    ciphertext = read_file(ciphertext_file_path)

    # Decrypt using RSA private key and PKCS#1 v1.5 padding
    plaintext_decrypted = decrypt_with_rsa_private_key_pem(rsa_private_key_pem, ciphertext)

    # Write the decrypted text to the file
    write_to_file(decryptedtext_file_path, plaintext_decrypted)
    print("Decryption complete.")
