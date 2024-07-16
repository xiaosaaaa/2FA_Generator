from flask import Flask, render_template, jsonify, request, url_for
import pyotp
from dotenv import load_dotenv
import os
import time
import qrcode
from io import BytesIO
import base64
from PIL import Image

# 加载环境变量
load_dotenv()

app = Flask(__name__)

def is_valid_secret(secret):
    return secret and len(secret) >= 16

def generate_qr_code(secret):
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(name='Free', issuer_name='2FA_Generator')
    qr = qrcode.make(uri)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

@app.route('/')
def index():
    secrets = {f'secret{i}': os.getenv(f'SECRET_KEY{i}') for i in range(1, 5)}
    codes = {f'code{i}': None for i in range(1, 5)}

    for i in range(1, 5):
        if is_valid_secret(secrets[f'secret{i}']):
            totp = pyotp.TOTP(secrets[f'secret{i}'])
            codes[f'code{i}'] = totp.now()

    remaining_time = 30 - (int(time.time()) % 30)
    show_countdown = any(codes.values())
    return render_template('index.html', **codes, remaining_time=remaining_time, show_countdown=show_countdown)

@app.route('/get_codes')
def get_codes():
    secrets = {f'secret{i}': os.getenv(f'SECRET_KEY{i}') for i in range(1, 5)}
    codes = {f'code{i}': None for i in range(1, 5)}

    for i in range(1, 5):
        if is_valid_secret(secrets[f'secret{i}']):
            totp = pyotp.TOTP(secrets[f'secret{i}'])
            codes[f'code{i}'] = totp.now()

    return jsonify(codes)

@app.route('/generate_code', methods=['POST'])
def generate_code():
    new_secret = request.form['new_secret']
    if not is_valid_secret(new_secret):
        return jsonify(error="Invalid secret"), 400
    totp = pyotp.TOTP(new_secret)
    new_code = totp.now()
    qr_code = generate_qr_code(new_secret)
    return jsonify(new_code=new_code, qr_code=qr_code)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12281)

