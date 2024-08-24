# import os


# inputan = input("masukkan input : ")
# if inputan == "ls":
#     print(os.system("open -a Visual\ Studio\ Code"))
import os

# Contoh 1: Memeriksa apakah file "example.txt" ada
file_path = "/Users/mahdi/Desktop/pemograman/pythonProject1/libyrary\ os/baso.py"
if not os.path.exists(file_path):
    print(f"File '{file_path}' ada.")
else:
    print(f"File '{file_path}' tidak ditemukan.")
baso = "walkk.py"
print(os.path.getsize(baso))






# Contoh 2: Memeriksa apakah direktori "my_folder" ada
