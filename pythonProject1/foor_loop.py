baso = [1,2,3,4,5]
for has in baso:
    print(f"angka {has}")

fruits = ["apel", "mangga", "pisang"]

for baso, fruit in enumerate(fruits):
    print(baso, fruit)

# perulangan bercabang
for i in range(1,6):
    for b in range(1,4):
        print(i,b)

matriks = [
    [1, 2, 3],
    [4, 5, 6]
]

# For bercabang untuk mengakses setiap elemen dalam matriks
for baris in matriks:
    for element in baris:
        print(element)



