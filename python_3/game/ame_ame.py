import time
from datetime import datetime, timedelta

def check_password():
    password = "rahasia"
    attempt = input("Masukkan password: ")
    confirm = input("Konfirmasi password: ")
    if attempt == password and confirm == password:
        return True
    else:
        print("Password salah atau tidak cocok!")
        return False

def kasir(menu):
    total = 0
    pesanan = []
    start_time = time.time()  # Mulai timer
    while True:
        item = input("Masukkan nama makanan atau 'selesai' untuk total: ")
        if item.lower() == 'selesai':
            break
        if item in menu:
            total += menu[item]
            pesanan.append(item)
            print(f"{item} berhasil ditambahkan. Subtotal: Rp{total}")
        else:
            print("Item tidak tersedia.")
    elapsed_time = time.time() - start_time  # Hitung waktu yang telah berlalu
    print("Pesanan Anda:")
    for makan in pesanan:
        print(f"- {makan}")
    print(f"Total belanjaan Anda adalah: Rp{total}")
    print(f"Waktu yang dibutuhkan untuk transaksi: {elapsed_time:.2f} detik")
    return total, pesanan

def tampilkan_menu():
    menu = {
        'Nasi Goreng': 15000,
        'Mie Ayam': 12000,
        'Sate Ayam': 20000
    }
    print("Menu Makanan:")
    for makanan, harga in menu.items():
        print(f"{makanan}: Rp{harga}")
    return menu

def waktu_masak(makanan):
    waktu = {
        'Nasi Goreng': 10,
        'Mie Ayam': 8,
        'Sate Ayam': 15
    }
    return waktu.get(makanan, "Tidak diketahui")

def countdown_timer(waktu, makanan):
    end_time = datetime.now() + timedelta(seconds=waktu)
    while datetime.now() < end_time:
        remaining_time = end_time - datetime.now()
        print(f"Sisa waktu masak {makanan}: {str(remaining_time).split('.')[0]}", end='\r')
        time.sleep(1)
    print(f"\n{makanan} telah selesai dimasak!")

def main():
    if check_password():
        print("Selamat datang di Aplikasi Kasir Terminal!")
        menu = tampilkan_menu()
        total, pesanan = kasir(menu)
        for item in pesanan:
            waktu = waktu_masak(item)
            if waktu != "Tidak diketahui":
                countdown_timer(waktu, item)
    else:
        print("Akses ditolak.")

if __name__ == "__main__":
    main()