import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3): # Duyệt qua 3 kênh màu (R, G, B)
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển đổi chuỗi nhị phân thành chuỗi ký tự
    message = ""
    for i in range(0, len(binary_message), 8):
        # Chuyển đổi từng 8 bit thành một ký tự
        byte = binary_message[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        
        # Kết thúc thông điệp khi gặp ký tự null '\0'
        if char == '\0':
            break
        message += char

    return message

def main():
    """
    Hàm chính để thực thi chương trình từ dòng lệnh.
    """
    # Kiểm tra xem người dùng có cung cấp đủ tham số dòng lệnh không
    if len(sys.argv) != 2:
        print("Cách sử dụng: python decrypt.py <đường_dẫn_tới_ảnh>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Thông điệp đã giải mã:", decoded_message)

# Điểm bắt đầu chạy chương trình
if __name__ == "__main__":
    main()