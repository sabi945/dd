users = {
    "kunci pagar": {
        "nama": "mahdi",
        "kelas": "10",
        "sekolah": "10 makassar",
    },
    "kunci pagar1": {
        "nama": "baso",
        "kelas": "13",
        "sekolah": "15 makassar",
    }
}

for user, statu in users.copy().items():
    status = statu["nama"]
    if status == "mahdi":
        del users[user]

users["kelas"] = "19"
print(users)

for key, data in users.items():
    nama = data["nama"]
    kelas = data["kelas"]
    print(f"nama {nama}, kelas {kelas}")
