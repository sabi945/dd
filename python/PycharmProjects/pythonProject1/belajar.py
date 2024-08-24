# Membuat list kosong untuk menyimpan inputan
my_list = []

# Membuat kondisi awal untuk loop while
selesai = False

while not selesai:
    # Membaca input dari pengguna
    inputan = input("Masukkan sesuatu (ketik 'selesai' untuk keluar): ")

    # Memeriksa apakah pengguna ingin keluar
    if inputan.lower() == 'selesai':
        selesai = True
    else:
        # Menambahkan inputan ke dalam list
        my_list.append(inputan)

# Loop while akan berhenti ketika 'selesai' dimasukkan
# Kemudian, kamu bisa melakukan apa pun yang kamu inginkan dengan list my_list
print("Inputan yang telah dimasukkan:")
for item in my_list:
    print(item)
