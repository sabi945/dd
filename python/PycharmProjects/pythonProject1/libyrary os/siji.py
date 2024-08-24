import os

# Dapatkan jalur absolut folder "libyrary os"
abs_path = os.path.abspath("heps")

# Dapatkan daftar file dan direktori di folder "libyrary os"
files = os.listdir("heps")

# Cetak daftar file dan direktori
for file in files:
    print(file)
