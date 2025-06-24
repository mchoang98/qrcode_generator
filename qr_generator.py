from PIL import Image
import qrcode
import requests
from io import BytesIO
import os

def tao_qr_logo(noi_dung, kich_thuoc=800, logo_path=None, logo_scale=0.2, output_path="static/output/qr.png"):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(noi_dung)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    try:
        resample = Image.Resampling.LANCZOS
    except:
        resample = Image.LANCZOS

    img_qr = img_qr.resize((kich_thuoc, kich_thuoc), resample=resample)

    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")
        logo_size = int(kich_thuoc * logo_scale)
        logo = logo.resize((logo_size, logo_size), resample=resample)
        pos = ((img_qr.width - logo.width) // 2, (img_qr.height - logo.height) // 2)
        img_qr.paste(logo, pos, mask=logo)

    img_qr.save(output_path)
    return output_path
