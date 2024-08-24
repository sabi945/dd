import pyautogui
import time

# Mendapatkan ukuran layar
screen_width, screen_height = pyautogui.size()

# Menentukan posisi yang ingin dicapai
target_x = 500
target_y = 300

# Menggunakan moveTo untuk memindahkan kursor ke posisi target dengan durasi animasi 1 detik
pyautogui.moveTo(target_x, target_y, duration=1)

# Menunggu sebentar untuk melihat hasilnya
time.sleep(2)

# Menggunakan write untuk mengetik teks
pyautogui.write("Hello, PyAutoGUI!")

# Menunggu sebentar untuk melihat hasilnya
time.sleep(2)
