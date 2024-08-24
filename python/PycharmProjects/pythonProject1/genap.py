numbers = [23, 10, 55, 78, 32, 45, 67, 12, 98, 34]

# Inisialisasi variabel untuk menyimpan bilangan terbesar
bilangan_terbesar = numbers[0]

# Menggunakan loop for untuk mencari bilangan terbesar
for num in numbers:
    if num > bilangan_terbesar:
        bilangan_terbesar = num

# Cetak hasil
print("Bilangan terbesar:", bilangan_terbesar)
