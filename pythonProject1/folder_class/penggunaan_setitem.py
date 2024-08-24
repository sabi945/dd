class DaftarPintar:
    def __init__(self):
        self.data = {}

    def __setitem__(self, kunci, nilai):
        self.data[kunci] = nilai

    def __getitem__(self, kunci):
        return self.data[kunci]

    def __len__(self):
        return len(self.data)

# Membuat objek DaftarPintar
daftar_saya = DaftarPintar()

# Mengisi objek DaftarPintar
daftar_saya[0] = "Nilai Pertama"
daftar_saya[1] = "Nilai Kedua"
# Melakukan iterasi melalui objek menggunakan loop for
for indeks in range(len(daftar_saya)):
    nilai = daftar_saya[indeks]
    print(f"Indeks {indeks}: {nilai}")
print(daftar_saya[0])