from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization


def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    """Tạo cặp khóa (private/public) cho máy chủ."""
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    """Hàm chính: tạo tham số, tạo khóa và lưu khóa công khai."""
    # Tạo tham số Diffie-Hellman. Trong thực tế, các tham số này
    # thường được thống nhất trước hoặc được gửi từ máy chủ.
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    
    # Tạo cặp khóa cho máy chủ
    private_key, public_key = generate_server_key_pair(parameters)

    # In ra thông báo để biết quá trình đang diễn ra
    print("Đã tạo cặp khóa thành công.")
    
    # Lưu khóa công khai vào một tệp .pem
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    
    print("Đã lưu khóa công khai vào tệp 'server_public_key.pem'.")

# Điểm bắt đầu của chương trình
if __name__ == "__main__":
    main()