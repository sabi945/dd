# baso = [1,2,3,4]
# tulisan = ["a", "b","c"]

# for sji in baso:
#     for halo in tulisan:
#         print(sji, halo)

# basi = "  baso, siji"
# hasil = basi.split(",   ")
# print(hasil)

inputan = input("masukkan jumlah baris : ")
N = int(input("masukkan angka nya : "))
for baso in range(N + 1):

    print(inputan * baso)

