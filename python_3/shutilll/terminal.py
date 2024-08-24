import shutil
import textwrap

# Mendapatkan ukuran terminal
size = shutil.get_terminal_size()

# Teks yang lebih panjang dari lebar terminal
long_text = "Ini adalah contoh teks yang panjangnya lebih dari delapan puluh karakter sehingga akan dibungkus ke baris berikutnya oleh terminal secara otomatis."

# Membungkus teks sesuai dengan lebar terminal
wrapped_text = textwrap.fill(long_text, width=size.columns)

# Menampilkan teks yang telah dibungkus
print(wrapped_text)
