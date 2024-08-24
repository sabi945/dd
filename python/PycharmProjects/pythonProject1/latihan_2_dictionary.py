dictionaryy = {
    "orang_1": {
        "nama": "baso",
        "kelas": "tujuh",
    },
    "orang_2": {
        "nama": "mahdi",
        "kelas": "sepuluh"
    }
}
dictionaryyy = {
    "nama": "kasi",
    "umur": "19"
}

# cara akses yang pertama
for i in dictionaryy:
    if i == "orang_1":
        nama = dictionaryy[i]
        eksekusi = nama["nama"]
        print(f"ini adalah nama yang anda minta : {eksekusi}")

# cara untuk memakai method keys()
eksekusi = dictionaryyy.keys()
print(eksekusi)

# cara mengakses tupple

