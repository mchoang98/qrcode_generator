# 🔲 QR Flat UI Generator — Flask Web App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/github/license/your-username/qr-flat-ui)](LICENSE)
[![QR Ready](https://img.shields.io/badge/QR--Style-Flat%20UI-green)](#)
[![Made with Love](https://img.shields.io/badge/Made%20with-%F0%9F%A4%8D%20by%20Anh%20Ph%C3%BA-red)](#)

> A modern Flask-based web app that generates beautiful, scannable **QR Codes** with embedded **logos**, following the **Flat UI** style. Supports file uploads and image URLs.

---

## 🚀 Features

- ✨ Clean, minimal Flat UI design
- 🔗 Upload logo or paste image URL
- 🖼️ Embeds logo at center of QR
- 📱 Generates high-quality, scannable QR codes
- ⚙️ Powered by `Flask`, `Pillow`, and `qrcode`

---

## 📸 Screenshot

<img src="screenshot.png" width="500" alt="screenshot" />

---

## 🧑‍💻 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/qr-flat-ui.git
cd qr-flat-ui

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
