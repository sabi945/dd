import tkinter as tk
from PIL import Image, ImageTk
import time
# Fungsi untuk menampilkan gambar
def show_image():
    # Buka gambar menggunakan Pillow
    image = Image.open("/Users/mahdi/Downloads/sharon-pittaway-iMdsjoiftZo-unsplash.jpg")

    # Konversi gambar ke format yang dapat digunakan oleh Tkinter
    tk_image = ImageTk.PhotoImage(image)

    # Tampilkan gambar di Label Tkinter
    image_label.config(image=tk_image)
    image_label.image = tk_image  # Ini penting untuk mencegah garbage collection
# Membuat jendela Tkinter
root = tk.Tk()
root.title("Contoh Menambahkan Gambar")
time.sleep(4)

# Tombol untuk menampilkan gambar
show_image_button = tk.Button(root, text="Tampilkan Gambar", command=show_image)
show_image_button.pack(pady=10)

# Label untuk menampilkan gambar
image_label = tk.Label(root)
image_label.pack()

# Jalankan loop utama Tkinter
root.mainloop()
