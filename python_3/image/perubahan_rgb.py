from PIL import Image
import numpy as np

# Lokasi direktori tempat Anda menyimpan foto
direktori_foto = "/Users/mahdi/Desktop/pemograman/python_3/image/"

# Nama file foto yang ingin Anda muat
nama_file_foto = "mahdi.png"

# Menggabungkan lokasi direktori dengan nama file foto
path_foto = direktori_foto + nama_file_foto

# Memuat foto menggunakan PIL
try:
    foto = Image.open(path_foto)
    foto_rgb = np.array(foto)  # Mengonversi gambar menjadi array NumPy RGB
    # Menggabungkan saluran warna menjadi satu gambar
    foto_asli = np.zeros_like(foto_rgb)
    foto_asli[:, :, 0] = foto_rgb[:, :, 0]  # Saluran merah
    foto_asli[:, :, 1] = foto_rgb[:, :, 1]  # Saluran hijau
    foto_asli[:, :, 2] = foto_rgb[:, :, 2]  # Saluran biru
    
    # Konversi array NumPy kembali menjadi gambar PIL
    foto_asli_pil = Image.fromarray(np.uint8(foto_asli))
    
    # Menyimpan gambar ke file
    foto_asli_pil.save("ff.png")
    print("Foto asli berhasil disimpan.")
except FileNotFoundError:
    print("File tidak ditemukan. Pastikan path_foto Anda sudah benar.")
except Exception as e:
    print("Terjadi kesalahan saat memuat foto:", str(e))
