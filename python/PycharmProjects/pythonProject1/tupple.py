#tupple adalah sebuah nilai yang tidak bisa di ubah di luar variabel tersebut
tupple_satu = ("baso","siji")
print(tupple_satu[0])

baso = "halo"
siji = "h"
pembuktian = siji in baso
print(pembuktian)


tupple_biodata = {
    ("siji"): 10,
    ("hasas"): 20
}
for i in tupple_biodata:
    halo = i
    score = tupple_biodata[halo]
    print(score)

#latihan dictionary awal
print("latihan dictionary awal")
data_1 = {
    "nama": "hasis",
    "nomor": 10
}

for baso in data_1:
    if baso == "nama":
        sccore = data_1[baso]
        print(sccore)
print("akhir dari dictionary awal")
#latihan sub-dictionary
data_2 = {
    "orang_1": {
        "nama": "baso",
        "kelas": 10,
    },
    "orang_2": {
        "nama": "mahdi",
        "kelas": 30,
    }
}
#cara untuk menampilkan dictionary dalam data_2
for bas in data_2:
    scroe = bas
    hasil = data_2[bas]
    print(hasil)

for ha in data_2:
    if ha == "orang_1":
        scor = data_2[ha]
        basoo = scor["nama"]
        print(basoo)
#cara mendapatkan isi dari orang 1 di luar for 
baso = data_2["orang_1"]["nama"]
print(baso)
