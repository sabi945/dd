import os

def akses_folder(folder_path, kunci_benar):
    # Minta pengguna memasukkan kata kunci
    kunci = input("Masukkan kata kunci untuk mengakses folder: ")
    
    # Cek apakah kata kunci yang dimasukkan benar
    if kunci == kunci_benar:
        # Jika benar, ubah direktori kerja ke folder yang ditentukan
        try:
            os.chdir(folder_path)
            print(f"Akses diterima. Anda sekarang berada di folder: {os.getcwd()}")
        except FileNotFoundError:
            print(f"Folder '{folder_path}' tidak ditemukan.")
        except PermissionError:
            print(f"Anda tidak memiliki izin untuk mengakses folder '{folder_path}'.")
    else:
        # Jika salah, beri tahu pengguna bahwa akses ditolak
        print("Kata kunci salah. Akses ditolak.")

if __name__ == "__main__":
    # Tentukan path folder yang ingin diakses dan kata kunci yang benar
    folder_path = '/Users/mahdi/Desktop/pemograman/python_3/oss'  # Ganti dengan path folder yang ingin diakses
    kunci_benar = '1234'            # Ganti dengan kata kunci yang benar
    
    # Panggil fungsi akses_folder
    akses_folder(folder_path, kunci_benar)
