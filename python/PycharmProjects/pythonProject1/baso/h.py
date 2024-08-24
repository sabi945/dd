class DaftarKontak:
    def __init__(self):
        self.kontak = {}

    def tambah_kontak(self, nama, nomor):
        self.kontak[nama] = nomor

    def cari_kontak(self, kriteria):
        if kriteria in self.kontak:
            return f"Nama: {kriteria}, Nomor: {self.kontak[kriteria]}"
        elif kriteria in self.kontak.values():
            for nama, nomor in self.kontak.items():
                if nomor == kriteria:
                    return f"Nama: {nama}, Nomor: {nomor}"
        return "Kontak tidak ditemukan."

# Membuat objek dari kelas DaftarKontak
daftar_kontak = DaftarKontak()

while True:
    print("Menu:")
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nomor = input("Masukkan nomor telepon: ")
        daftar_kontak.tambah_kontak(nama, nomor)
        print("Kontak berhasil ditambahkan.\n")
    elif pilihan == "2":
        kriteria = input("Masukkan nama atau nomor yang ingin dicari: ")
        hasil_cari = daftar_kontak.cari_kontak(kriteria)
        print(hasil_cari + "\n")
    elif pilihan == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
