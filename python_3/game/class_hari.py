import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Data produk (bisa diambil dari database nantinya)
produk = {
    "Apel": 5000,
    "Jeruk": 4000,
    "Mangga": 8000,
    "Pisang": 3000,
    "Anggur": 10000
}

def login(event=None):  # Menambahkan parameter event
    password_benar = "rahasia"  # Ganti dengan password Anda
    password_coba = password_entry.get()

    if password_coba == password_benar:
        messagebox.showinfo("Berhasil", "Login berhasil!")
        login_frame.pack_forget()
        belanja()
    else:
        messagebox.showerror("Error", "Password salah!")

def belanja():
    def tambah_ke_keranjang():
        item = produk_combobox.get()
        jumlah = int(jumlah_spinbox.get())
        harga = produk[item] * jumlah
        keranjang_listbox.insert(tk.END, f"{item} x {jumlah} = Rp {harga}")
        total_harga_var.set(total_harga_var.get() + harga)

    def selesai_belanja():
        if keranjang_listbox.size() == 0:
            messagebox.showinfo("Info", "Keranjang belanja kosong.")
            return
        messagebox.showinfo("Pembayaran", f"Total harga: Rp {total_harga_var.get()}")
        # Di sini Anda bisa menambahkan logika untuk memproses pembayaran
        window_belanja.destroy()

    window_belanja = ttk.Toplevel(window)
    window_belanja.title("Keranjang Belanja")

    ttk.Label(window_belanja, text="Pilih Produk:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    produk_combobox = ttk.Combobox(window_belanja, values=list(produk.keys()))
    produk_combobox.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(window_belanja, text="Jumlah:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    jumlah_spinbox = ttk.Spinbox(window_belanja, from_=1, to=10)
    jumlah_spinbox.grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(window_belanja, text="Tambah ke Keranjang", command=tambah_ke_keranjang).grid(row=2, column=0, columnspan=2, pady=10)

    keranjang_listbox = tk.Listbox(window_belanja)
    keranjang_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    total_harga_var = tk.IntVar(value=0)
    ttk.Label(window_belanja, text="Total Harga:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(window_belanja, textvariable=total_harga_var).grid(row=4, column=1, padx=5, pady=5)

    ttk.Button(window_belanja, text="Selesai", command=selesai_belanja).grid(row=5, column=0, columnspan=2, pady=10)

window = ttk.Window(themename="superhero")
window.title("Sistem Perbelanjaan")

login_frame = ttk.Frame(window, padding="20")
login_frame.pack(padx=20, pady=20)

ttk.Label(login_frame, text="Masukkan Password:").pack()
password_entry = ttk.Entry(login_frame, show="*")
password_entry.pack()
password_entry.bind("<Return>", login)  # Menambahkan event binding untuk Enter

ttk.Button(login_frame, text="Login", command=login).pack(pady=10)

window.mainloop()
