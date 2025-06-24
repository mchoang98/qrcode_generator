from flask import Flask, render_template, request, redirect, url_for
from qr_generator import tao_qr_logo
import os
import requests
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'static/output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_path = None
    if request.method == 'POST':
        data = request.form.get('data')
        logo_url = request.form.get('logo_url')
        logo_file = request.files.get('logo_file')
        logo_path = None

        # Nếu người dùng upload file
        if logo_file and logo_file.filename:
            filename = os.path.join(UPLOAD_FOLDER, "uploaded_logo.png")
            logo_file.save(filename)
            logo_path = filename

        # Nếu người dùng nhập URL ảnh
        elif logo_url:
            try:
                resp = requests.get(logo_url)
                if resp.status_code == 200:
                    logo_path = os.path.join(UPLOAD_FOLDER, "downloaded_logo.png")
                    with open(logo_path, 'wb') as f:
                        f.write(resp.content)
            except:
                pass

        # Tạo QR nếu có dữ liệu
        if data:
            qr_path = tao_qr_logo(data, logo_path=logo_path)

    return render_template("index.html", qr_path=qr_path)

if __name__ == '__main__':
    app.run(debug=True)
