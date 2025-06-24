
# QR Flat UI Generator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/github/license/mchoang98/qrcode_generator)](LICENSE)

A modern Flask web app for generating high-quality QR codes with optional logo insertion.  
Flat UI style – minimal, clean, and scannable.

---

## Features

- Generate QR codes from text or URLs
- Upload a logo image or paste an image URL
- Logo placed at the center of QR (with optional border)
- Flat UI design — no background noise
- Output high-resolution PNG (800×800)
- Built using Flask, Pillow, qrcode, and requests

---

## Screenshot

> *(Replace the link below with your actual screenshot)*  
![Preview](screenshot.png)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mchoang98/qrcode_generator.git
cd qrcode_generator
```

### 2. Create a virtual environment (optional but recommended)

#### On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Then open your browser and go to:  
[http://localhost:5000](http://localhost:5000)

---

## Usage

1. Enter the text or URL to encode in the QR code
2. Upload a logo file (PNG/JPG) or paste an image URL
3. Click **Generate QR**
4. Download the QR code image

---

## Project Structure

```
qrcode_generator/
├── app.py               # Flask app
├── qr_generator.py      # QR creation logic
├── requirements.txt     # Dependencies
├── static/
│   └── output/          # Generated QR images
└── templates/
    └── index.html       # Web UI
```

---

## Dependencies

- Flask
- qrcode
- Pillow
- requests

Install them with:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the [MIT License](https://github.com/mchoang98/qrcode_generator/blob/main/LICENSE).

---

## Author

**Phu Hoang**  
[github.com/mchoang98](https://github.com/mchoang98)
