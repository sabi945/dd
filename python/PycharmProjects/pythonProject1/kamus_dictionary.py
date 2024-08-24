users = {
    "nama": "mahdi",
    "umur": "18",
    "class": "smk negeri 10 makassar"
}

for user, status in users.copy().items():
    if status == "mahdi":
        del users[user]

users["umur"] = "19"
print(users)
biodata = {
    "kunci pagar": {
        "nama": "mahdi",
        "usia": "26",
        "alamat": "makassar",
    },
    "kunci pagar 2": {
        "nama": "baso",
        "usia": "12",
        "alamat": "jakarta",

    }
}
for has in biodata:
    score = biodata[has]
    value = score["nama"]
    print(value)

orang_1 = biodata["kunci pagar"]["nama"]
print(f"nama : {orang_1}")


# cara mengguanakan method get

users_2 = {
    "nama": "baso",
    "kelas": "10",
    "alamat": "jl kelapa tiga",
}
# penggunaaan pertama untuk get
personal = users_2.get("nama")
print("nama = " + personal)

# penggunaan kedua untuk get
personal = users_2.get("unknown", "tidak ada")
print(f"unknown = {personal}")

# cara untuk memakai get dengan kunci double

biodata_1 = {
    "kunci pagar": {
        "nama": "mah",
        "usia": "26",
        "alamat": "makassar",
    },
    "kunci pagar 2": {
        "nama": "baso",
        "usia": "12",
        "alamat": "jakarta",
    }
}

personal_1 = biodata_1.get("kunci pagar", {}).get("nam", "kunci tidak ditemukan")
print(f"nama = {personal_1}")
# penjelasan tentang tanda "{}" di sebuah method get itu adalah sebuah nilai default apabila
# suatu kunci tidak ada di dalam dictionary tersebut maka akan memunculkan nilai default
# contoh apabila kunci yang bernama "kunci pagar" tidak ada di dalam dictionary maka akan memunculkan nilai default
# dan apabila "kunci pagar" itu ada di dalam dictionary dan sebaliknya jika "nama" tidak ada dalam
# "kunci pagar" tersebut maka akan memunculkan nilai defautl yang sama












