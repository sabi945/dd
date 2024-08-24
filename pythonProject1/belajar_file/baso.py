import os
# untuk membuat sebuah folder
# whilee = True
# while whilee:
#     inputan = input("buat folder baru : ")

#     path_nya = os.path.join(os.getcwd(),inputan)

#     if inputan == "exit":
#         break
#     elif not os.path.exists(path_nya):
#         os.mkdir(inputan)
#         print(f"folder berhasil di buat {inputan}")
#     else:
#         print(f"folder sudah ada {inputan}")

# untuk berpindah ke folder lain
# while True:
#     # Meminta input nama folder dari pengguna
#     inputan = input("Masukkan nama folder (atau ketik 'exit' untuk keluar): ")

#     # Jika pengguna memasukkan 'exit', keluar dari loop
#     if inputan.lower() == 'exit':
#         print("Keluar dari loop.")
#         break

#     # Mengecek apakah folder dengan nama yang diinputkan sudah ada
#     path_folder = os.path.join(os.getcwd(), inputan)

#     if os.path.exists(path_folder) and os.path.isdir(path_folder):
#         # Jika folder sudah ada, pindah ke folder tersebut
#         os.chdir(path_folder)
#         print(f"Berhasil berpindah ke folder: {path_folder}")
#     else:
#         # Jika folder tidak ada, berikan pesan
#         print(f"Folder dengan nama '{inputan}' tidak ditemukan.")
