biodata = {
    "nama": "mahdi",
    "umur": 8,
    "hobi": ["main bola", "main basket", "berenang"]
}
data = {
    "kelas": "10"
}
siji = biodata.update(data)


print(biodata)
set_satu = {1, 2, 9, 3, 4, 5}
set_dua = {3, 4, 5, 6, 7}

perbedaan = set_satu.difference_update(set_dua)

print(set_satu)


# inputan = input("masukkan nama anda : ")


# if inputan == biodata.get("nama", "nama tidak ada"):
#     usia_value = biodata["umur"]
#     print(f'nama : {inputan} usia : {usia_value}')
# else:
#     print("nama yang anda masukkan tidak ada dalam daftar")