import re

# Pola regex untuk mencari nomor telepon dengan format XXX-XXX-XXXX
pattern = r'\d{3}-\d{3}-\d{4}'

# Variabel dengan teks yang ingin Anda cocokkan
teks1 = "Nomor telepon pertama adalah 123-456-7890."
teks2 = "Nomor telepon kedua adalah 987-654-3210."

# Menggabungkan teks1 dan teks2 menjadi satu teks
teks_gabungan = teks1 + teks2

# Mencocokkan pola regex dari teks yang digabungkan
hasil = re.search(pattern, teks_gabungan)

# Menampilkan hasil
print("Hasil pencocokan:", hasil.group())



# Pola regex untuk mencari nomor telepon dengan format XXX-XXX-XXXX
pattern = r'\d{3}-\d{3}-\d{4}'

# Teks yang ingin Anda cocokkan
teks = "Nomor telepon: 123-456-7890."

# Mencocokkan pola regex dengan re.match()
hasil_match = re.match(pattern, teks)

if hasil_match:
    print("Pencocokan berhasil di awal string:", hasil_match.group())
else:
    print("Pencocokan gagal di awal string.")

# Pola regex untuk mencari nomor telepon dengan format XXX-XXX-XXXX
patte = r'\d{3}-\d{3}-\d{4}'

# Teks yang ingin Anda cocokkan
tek = "Nomor telepon pertama adalah 123-456-7890. Nomor telepon kedua adalah 987-654-3210."

# Menggunakan re.finditer() untuk mencocokkan pola regex
iterator = re.finditer(patte, tek)

for moderator in iterator:
    print("pencarian dari hal : ", moderator.group())

operatot = r'merah'
te = "mobil merah, bajai merah,motor merah"
hasi = re.sub(operatot,"biru",te)
print(f"ini adalah hasilnya : {hasi}")


teks_3 = "halo 192-169-4666"
teks_4 = "halo 495-454-7559"

penggabungan = re.finditer(patte,teks_3)

for baso in penggabungan:
    print(f"halo {baso.group()}")