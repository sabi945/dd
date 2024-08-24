import sys
import os
import numpy

# Dapatkan path file dari modul yang diimpor
file_path = sys.modules['numpy'].__file__

# Konversi ke path absolut
absolute_path = os.path.abspath(file_path)

# Tampilkan path absolut
print(absolute_path)


keranjang = {
    "aple":[1000,1]
}

text = "   Hello,    World!   "
clean_text = " ".join(text.split())
print(f"'{clean_text}'") 
my_dict = {'a': 1, 'b': 5}
print(my_dict.values('a'))        
print(my_dict.get('c', 0))     # Output: 0
 # Output: 'Hello, World!'

dictionary = {}
inputan = input("masukkan inputan anda di dalam sini : ")

key, value = inputan.split(":")
dictionary[key.strip()] = value.strip()
print(dictionary)



# import subprocess

# # Mendefinisikan perintah untuk menutup Microsoft Edge
# command = ['pkill', 'Hyper']

# # Menjalankan perintah menggunakan subprocess
# subprocess.run(command)
# print(__file__)
