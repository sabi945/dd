

# inputan = input("masukkan inputan : ")

# filenya = "h.py"
# shutil.move(filenya,inputan)
import shutil

# Tentukan path direktori yang ingin Anda periksa

path = "/Users/mahdi/Desktop/pemograman/python_3/oss"

# Panggil fungsi disk_usage
disk_usage = shutil.disk_usage(path)

# Fungsi untuk mengonversi bytes ke unit yang lebih mudah dibaca
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

# Cetak informasi penggunaan disk dengan unit yang disesuaikan
print(f"Total ruang disk: {convert_bytes(disk_usage.total)}")
print(f"Ruang disk yang telah digunakan: {convert_bytes(disk_usage.used)}")
print(f"Ruang disk yang tersedia: {convert_bytes(disk_usage.free)}")


