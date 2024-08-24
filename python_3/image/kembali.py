def find_maximum(A):
    # Inisialisasi nilai maksimum dengan elemen pertama array
    max_value = A[0]

    # Loop melalui setiap elemen dalam array mulai dari indeks 1 hingga akhir
    for i in range(1, len(A)):
        # Jika elemen saat ini lebih besar dari nilai maksimum saat ini
        if A[i] > max_value:
            # Update nilai maksimum
            max_value = A[i]

    # Kembalikan nilai maksimum
    return max_value

# Contoh penggunaan
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_value = find_maximum(array)
print("Nilai maksimum dalam array adalah:", max_value)
