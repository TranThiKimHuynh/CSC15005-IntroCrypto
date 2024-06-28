import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

def verify_file(public_key_pem_path, message_path, signature_path):
    with open(public_key_pem_path, 'rb') as f:
        public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())
    with open(message_path, 'rb') as f:
        message = f.read()
    with open(signature_path, 'rb') as f:
        signature = f.read()
    try:
        public_key.verify(signature, message, padding.PKCS1v15(), hashes.SHA256())
        print('File signature verified successfully.')
    except Exception as e:
        print(f'Signature verification failed: {e}')

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <mess_file_path> <sign_file_path> <pub_pem_file_path>")
        sys.exit(1)

    # Extract file paths from command-line arguments
    mess_file_path = sys.argv[1]
    sign_file_path = sys.argv[2]
    pub_pem_file_path = sys.argv[3]
    verify_file(pub_pem_file_path , mess_file_path, sign_file_path)
