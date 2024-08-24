import os
import time

# Tentukan path file yang ingin Anda periksa
file_path = "/Users/mahdi/Desktop/pemograman/python_3/oss       "

# Gunakan os.stat untuk mendapatkan informasi file
file_stats = os.stat(file_path)

# Waktu pembuatan file dalam format waktu Unix
creation_time = file_stats.st_ctime

# Konversi waktu Unix ke format yang mudah dibaca
readable_creation_time = time.ctime(creation_time)

# Cetak waktu pembuatan file
print(f"Waktu pembuatan file: {readable_creation_time}")