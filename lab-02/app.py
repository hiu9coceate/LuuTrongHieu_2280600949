from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
import subprocess
import os

app = Flask(__name__, template_folder='Templates')

#HOME 
@app.route("/")
def home():
    return render_template("index.html")


#CAESAR
@app.route("/caesar")
def caesar():
    caesar_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03', 'caesar_cipher.py')
    
    try:
        # Sử dụng cmd để giữ cửa sổ mở
        os.system(f'start cmd /k "python "{caesar_path}""')
        return "Bấm lùi trang để thử mã hoá khác..."
    except Exception as e:
        return f"Error launching application: {str(e)}"

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"


#VIGENERE 
@app.route("/vigenere")
def vigenere():
    caesar_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03', 'vigenere_cipher.py')
    
    try:
        # Sử dụng cmd để giữ cửa sổ mở
        os.system(f'start cmd /k "python "{caesar_path}""')
        return "Bấm lùi trang để thử mã hoá khác..."
    except Exception as e:
        return f"Error launching application: {str(e)}"

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"


#RAILFENCE 
@app.route("/railfence")
def railfence():
    caesar_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03', 'railfence_cipher.py')
    
    try:
        # Sử dụng cmd để giữ cửa sổ mở
        os.system(f'start cmd /k "python "{caesar_path}""')
        return "Bấm lùi trang để thử mã hoá khác..."
    except Exception as e:
        return f"Error launching application: {str(e)}"

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    rail = RailFenceCipher()
    encrypted_text = rail.rail_fence_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    rail = RailFenceCipher()
    decrypted_text = rail.rail_fence_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"


#  PLAYFAIR
@app.route("/playfair")
def playfair():
    caesar_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03', 'playfair_cipher.py')
    
    try:
        # Sử dụng cmd để giữ cửa sổ mở
        os.system(f'start cmd /k "python "{caesar_path}""')
        return "Bấm lùi trang để thử mã hoá khác"
    except Exception as e:
        return f"Error launching application: {str(e)}"

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"




# ===================== RUN =====================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)