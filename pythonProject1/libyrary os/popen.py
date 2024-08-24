import os

# Membuka file
file_path = 'example.txt'
file_descriptor = os.open(file_path, os.O_RDWR | os.O_CREAT)

# Menulis data ke file
os.write(file_descriptor, b'Hello, World!')

# Menutup file descriptor menggunakan os.close
os.close(file_descriptor)

# Membuka file lagi
file_descriptor = os.open(file_path, os.O_RDWR)

# Membaca data dari file
data = os.read(file_descriptor, 1024)
print(data.decode('utf-8'))

# Menutup file descriptor setelah digunakan
os.close(file_descriptor)
