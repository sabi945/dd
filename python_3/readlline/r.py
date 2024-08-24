import readline

# Fungsi untuk menampilkan menu
def show_menu():
    print("\nMenu:")
    print("1. Masukkan perintah")
    print("2. Tampilkan riwayat")
    print("3. Hapus riwayat")
    print("4. Keluar")

# Fungsi untuk menampilkan riwayat input
def show_history():
    print("\nRiwayat Input:")
    for i in range(readline.get_current_history_length()):
        print(f"{i + 1}: {readline.get_history_item(i + 1)}")

# Program utama
while True:
    show_menu()
    choice = input("Pilih opsi: ")

    if choice == '1':
        command = input("Masukkan perintah: ")
        readline.add_history(command)
    elif choice == '2':
        show_history()
    elif choice == '3':
        readline.clear_history()
        print("Riwayat telah dihapus.")
    elif choice == '4':
        print("Keluar dari program.")
        break
    else:
        print("Opsi tidak valid. Silakan coba lagi.")
