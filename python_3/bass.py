# import os

# inputan = input("cari file kamu : ")
# pemanggil = os.path.abspath(inputan)
# if os.path.exists(pemanggil):
#     print(f"hasil nya {pemanggil}")
# else:
#     print(f"ups file {inputan} tidak ada")
import glob
import os

nama_file = input("Masukkan nama file yang ingin Anda cari: ")  # Input dari pengguna
pola_pencarian = f"**/{nama_file}"

list_file = glob.glob(pola_pencarian, recursive=True)

if list_file:
    home_dir = os.path.expanduser("~")
    for lokasi_file in list_file:
        relatif_path = os.path.relpath(lokasi_file, home_dir)
        print(f"File '{nama_file}' ditemukan di: ~/{relatif_path}")
else:
    print(f"File '{nama_file}' tidak ditemukan.")


