# QR Flat UI Generator


[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/github/license/mchoang98/qrcode_generator)](LICENSE)
[![QR Style](https://img.shields.io/badge/QR--Style-Flat%20UI-green)](#)
[![Made by Phu Hoang](https://img.shields.io/badge/Made%20by-Phu%20Hoang-red)](#)

A modern Flask-based web app that generates clean, scannable **QR codes** with embedded **logos**, following the Flat UI design style.

---

## Features

- Flat UI design — minimal and clean  
- Upload logo or paste image URL  
- Logo placed at center of QR code  
- High-resolution PNG output (800×800)  
- Built with Flask, Pillow, qrcode, requests

---

## Screenshot

![Preview](screenshot.png) <!-- Replace with actual screenshot -->

---

## Installation

```bash
git clone https://github.com/mchoang98/qrcode_generator.git
cd qrcode_generator

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
