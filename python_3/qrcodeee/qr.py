import qrcode
import os
import uuid

def create_qr_code():
    # Meminta user memasukkan URL
    url = input("Masukkan URL yang ingin dimasukkan ke dalam QR code: ")

    # Membuat instance dari QRCode
    qr = qrcode.QRCode(
        version=10,  # ukuran dari QR code, versi 1 adalah yang terkecil
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # tingkat koreksi kesalahan
        box_size=10,  # ukuran kotak per pixel dalam QR code
        border=4,  # ukuran border dari QR code
    )

    # Menambahkan data ke dalam QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Membuat gambar QR code
    img = qr.make_image(fill='black', back_color='white')

    # Membuat nama file yang acak menggunakan uuid
    file_name = f"qrcode_{uuid.uuid4().hex}.png"
    save_path = f"/Users/mahdi/Desktop/pemograman/python_3/qrcodeee/{file_name}"

    # Menyimpan gambar QR code
    img.save(save_path)

    print(f"QR code berhasil dibuat dan disimpan sebagai {save_path}")

while True:
    create_qr_code()
    lagi = input("Apakah Anda ingin membuat QR code lagi? (y/n): ").strip().lower()
    if lagi != 'y':
        break
