data_awal = {
    "orang_1": {
        "nama": "hasimi",
        "umur": 10
    },
    "orang_2": {
        "nama": "sinju",
        "umur": 38,
    }
}
#langkah pertama
masuk = data_awal["orang_1"]
masuk_1 = masuk["nama"]
print(masuk_1)
print("===============")
#langkah kedua
for i in data_awal:
    if i == "orang_1":
        nama = data_awal[i]
        hasil = nama["nama"]
        print(hasil)

data_tupple = {
    ("baso", "siji"): "bakso",
    ("halo", "adakah"): "baksis",
}
for b in data_tupple:
    first_name, last_name = b
    print(f"nama : {first_name}")

print("===========")
for c in data_tupple:
    if c[0] == "baso":
         print(data_tupple[c])
         break