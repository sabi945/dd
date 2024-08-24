from prettytable import PrettyTable
import bcrypt as bc
def has_password(password):
    simpan = bc.gensalt(rounds=12)
    hasing = bc.hashpw(password.encode('utf-8'),simpan)
    return hasing

# Data buah dan harganya
buah_data = {
    "apple": 10000,
    "rambutan": 5000,
    "pisang": 10000,
    "cherry": 20000
}

# Tabel untuk menampilkan daftar buah
tabel = PrettyTable()
tabel.field_names = ["Buah", "Harga"]
for buah, harga in buah_data.items():
    tabel.add_row([buah, harga])

# Keranjang belanja untuk menyimpan item yang dipilih pengguna
keranjang = {}
password = "mahdi"
masuk = input("masukkan user : ")
if masuk == "root":
    password_users = input("masukkan pasword : ")
    hasnya = has_password(password)
    if bc.checkpw(password_users.encode('utf-8'),hasnya):        
        while True:
            inputan = input("Apa yang kamu beli (buah peralatan teknologi): ")
            if inputan == "exit":
                break

            if inputan == "buah":
                while True:
                    masuk_input = input("Masukkan nama buah yang kamu mau (-list untuk melihat daftar, -total untuk melihat total harga, -exit untuk keluar): ")
                    
                    if masuk_input == "list":
                        print(tabel)
                    
                    elif masuk_input in buah_data:
                        jumlah_buah = int(input(f"Berapa banyak {masuk_input} yang ingin kamu beli? "))
                        if masuk_input in keranjang:
                            keranjang[masuk_input][1] += jumlah_buah
                        else:
                            keranjang[masuk_input] = [buah_data[masuk_input], jumlah_buah]
                            print(f"{masuk_input} telah ditambahkan ke keranjang.")
                    elif masuk_input == "total":
                        total_harga = sum(harga * jumlah for buah ,(harga, jumlah) in keranjang.items())
                        print(f"Total harga: {total_harga}")
                    
                    elif masuk_input == "exit":
                        print("Terima kasih sudah berbelanja. Byee!")
                        break
                    
                    elif masuk_input == "lihat":
                        print(keranjang)
                    else:
                        print("Inputan salah atau buah tidak tersedia!")
                
                # Tampilkan total harga terakhir saat keluar
                total_harga = sum(harga * jumlah for buah, (harga, jumlah) in keranjang.items())
                print("\nKeranjang Belanja Anda:")
                for buah, (harga, jumlah) in keranjang.items():
                    print(f"{buah}: {jumlah} x {harga} = {jumlah * harga}")
                print(f"Total harga akhir: {total_harga}")

            else:
                print("Kategori yang dipilih tidak tersedia.")
    else:
        print("upss password anda salah!")