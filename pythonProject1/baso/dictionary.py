# Inisialisasi dictionary kosong
my_dict = {}

# Minta pengguna untuk memasukkan pasangan kunci dan nilai
while True:
    key = input("Masukkan kunci (tekan Enter untuk selesai): ")
    if key == "exit":
        break
    value = input("Masukkan nilai: ")
    my_dict[key] = value

# Tampilkan dictionary yang telah dibuat
print("Dictionary hasil:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
