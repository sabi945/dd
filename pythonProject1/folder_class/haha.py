import tkinter as tk
from tkinter import messagebox

def save_note():
    note_text = text_entry.get("1.0", "end-1c")  # Mendapatkan teks dari widget teks
    if note_text:
        with open("note.txt", "w") as file:
            file.write(note_text)
        messagebox.showinfo("Catatan Disimpan", "Catatan berhasil disimpan!")
    else:
        messagebox.showwarning("Peringatan", "Catatan kosong. Silakan tulis sesuatu.")

def load_note():
    try:
        with open("note.txt", "r") as file:
            note_text = file.read()
            text_entry.delete("1.0", tk.END)  # Menghapus teks yang ada
            text_entry.insert("1.0", note_text)  # Menampilkan catatan yang dimuat
    except FileNotFoundError:
        messagebox.showwarning("Peringatan", "Tidak ada catatan yang tersimpan.")

# Membuat objek Tkinter
root = tk.Tk()
root.title("Aplikasi Catatan")
root.resizable(False,False)

# Membuat widget teks untuk input catatan
text_entry = tk.Text(root, wrap="word", width=40, height=10)
text_entry.pack(padx=10, pady=10)

# Membuat tombol untuk menyimpan catatan
save_button = tk.Button(root, text="Simpan Catatan", command=save_note)
save_button.pack(pady=5)

# Membuat tombol untuk memuat catatan
load_button = tk.Button(root, text="Muat Catatan", command=load_note)
load_button.pack(pady=5)

# Menjalankan loop utama Tkinter
root.mainloop()
