import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    pixel_index = 0
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110' # Đánh dấu kết thúc thông điệp
    import sys
    data_index = 0
    
    # Lặp qua từng pixel của ảnh
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))

            # Lặp qua các kênh màu (R, G, B)
            for color_channel in range(3):
                if data_index < len(binary_message):
                    # Thay đổi bit cuối cùng của kênh màu
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            
            img.putpixel((col, row), tuple(pixel))

            # Nếu đã giấu hết thông điệp thì dừng lại
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print(f"Hoàn tất Steganography. Hình ảnh đã mã hóa được lưu tại: {encoded_image_path}")

def main():
    # Kiểm tra các đối số dòng lệnh
    if len(sys.argv) != 3:
        print("Sử dụng: python ten_file.py <duong_dan_anh> \"<thong_diep>\"")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()