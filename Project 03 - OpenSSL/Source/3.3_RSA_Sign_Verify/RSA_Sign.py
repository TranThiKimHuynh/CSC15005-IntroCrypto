import sys
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
def sign_with_rsa_private_key_pem(rsa_private_key_pem, message):
    # Chuyển đổi khóa bí mật RSA từ định dạng PEM
    rsa_private_key = serialization.load_pem_private_key(
        rsa_private_key_pem.encode(),
        password=None,
        backend=default_backend()
    )

    # Ký điều thông điệp bằng khóa bí mật RSA và thuật toán hash SHA-256
    # Sign the message with PKCS1v15 padding
    signature = rsa_private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return signature

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_to_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <mess_file_path> <sign_file_path> <priv_pem_file_path>")
        sys.exit(1)

    # Extract file paths from command-line arguments
    mess_file_path = sys.argv[1]
    sign_file_path = sys.argv[2]
    priv_pem_file_path = sys.argv[3]

    # Sử dụng khóa bí mật RSA từ priv.pem
    with open(priv_pem_file_path, 'rb') as f:
        rsa_private_key_pem = f.read().decode()

    # Đọc nội dung từ tệp mess.txt (nơi bạn lưu nội dung cần ký)
    message = read_file(mess_file_path)

    # Ký điều thông điệp bằng khóa bí mật RSA và thuật toán hash SHA-256
    signature = sign_with_rsa_private_key_pem(rsa_private_key_pem, message)

    # Ghi kết quả chữ ký ra tệp sign1.txt
    write_to_file(sign_file_path, signature)
    print("Signature successfully generated.")



