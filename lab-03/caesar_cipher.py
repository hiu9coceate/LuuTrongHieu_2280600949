# caesar_cipher.py
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Lấy đường dẫn tuyệt đối đến thư mục chứa file hiện tại
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Tạo đường dẫn đến file UI
        ui_file = os.path.join(current_dir, "ui", "caesar.ui")
        
        # Kiểm tra xem file UI có tồn tại không
        if not os.path.exists(ui_file):
            raise FileNotFoundError(f"Không tìm thấy file UI tại: {ui_file}")
            
        self.ui = uic.loadUi(ui_file, self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)
        self.show()

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.textEdit_2.toPlainText(),
            "key": self.ui.textEdit_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                # Dòng này được suy luận dựa trên ngữ cảnh tương tự với phần giải mã
                # msg.setText("Encrypted Successfully") # Có thể thiếu trong ảnh gốc
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            # Trong ảnh, ".message" có thể là ".args[0]" tùy phiên bản requests
            # Hoặc có thể là lỗi đánh máy trong sách. Giữ nguyên theo ảnh.
            print("Error: %s" % e.message)


    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            # Giả định trường payload dựa trên ngữ cảnh của hàm giải mã
            "cipher_text": self.ui.textEdit.toPlainText(),
            "key": self.ui.textEdit_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_2.setText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
          
            print("Error: %s" % e.message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())