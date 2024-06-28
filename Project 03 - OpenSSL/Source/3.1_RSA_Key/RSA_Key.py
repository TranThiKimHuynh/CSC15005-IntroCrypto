import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def read_key_file(file_path):
    with open(file_path, 'rb') as key_file:
        key_data = key_file.read()
        return key_data

def extract_rsa_components_private_key(key_data):
    try:
        private_key = serialization.load_pem_private_key(
            key_data,
            password=None,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # Extract components
        n = public_key.public_numbers().n
        e = public_key.public_numbers().e
        d = private_key.private_numbers().d

        print(f"Modulus (n): {n}")
        print(f"Public Exponent (e): {e}")
        print(f"Private Exponent (d): {d}")

    except ValueError as e:
        print(f"Error extracting components: {e}")

def extract_rsa_components_public_key(key_data):
    try:
        public_key = serialization.load_pem_public_key(
            key_data,
            backend=default_backend()
        )

        # Extract components
        n = public_key.public_numbers().n
        e = public_key.public_numbers().e

        print(f"Modulus (n): {n}")
        print(f"Public Exponent (e): {e}")

    except ValueError as e:
        print(f"Error extracting components: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py must have <private_key_path>  <public_key_path>")
        sys.exit(1)

    # Extract file paths from command-line arguments
    private_key_file_path = sys.argv[1]
    public_key_file_path = sys.argv[2]

    # Read the key data from the files
    private_key_data = read_key_file(private_key_file_path)
    public_key_data = read_key_file(public_key_file_path)

    # Extract components of the private key
    print("Private Key Components:")
    extract_rsa_components_private_key(private_key_data)

    # Extract components of the public key
    print("\nPublic Key Components:")
    extract_rsa_components_public_key(public_key_data)
