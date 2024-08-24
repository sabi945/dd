

# path = "/Users/mahdi/Desktop/pemograman/python_3/hapus"

# hapus = shutil.rmtree(path)



import shutil

# Input dari pengguna
input_data = input("Masukkan perintah (cv, sumber, tujuan): ")
aksi, sumber, tujuan = input_data.split(",")

# Memeriksa apakah tindakannya adalah "cv"
if aksi == "cv":
  # Menggunakan shutil.move untuk memindahkan file
  try:
    shutil.move(sumber, tujuan)
    print(f"File atau folder berhasil dipindahkan dari {sumber} ke {tujuan}")
  except Exception as e:
    print(f"Terjadi kesalahan saat memindahkan: {e}")
else:
  print("Aksi yang tidak valid. Harap masukkan 'cv' untuk memindahkan.")
# Users/mahdi/Desktop/pemograman/python_3/project_kivy
# Users/mahdi/Desktop/pemograman/python_3/shutilll
