# def Matematika(opsi):
#     def tambah(x, y):
#         return x + y
#     def kurang(a, u):
#         return a - u
#     if opsi == "tambah":
#         return tambah
#     elif opsi == "kurang":
#         return kurang
        
# print("======= hanya ada dua opsi yaitu tambah dan kurang =======")
# masukan = input("masukkan operator : ")
# panggilan = Matematika(masukan)

# inputan_1 = int(input("masukkan angka pertama : "))
# inputan_2 = int(input("masukkan angka ke dua : "))

# panggilan_2 = panggilan(inputan_1,inputan_2)
# print(panggilan_2)

import json

# Contoh objek Python
data = {
    "nama": "John",
    "umur": 30,
    "kota": "New York"
}

# Mengonversi objek Python ke JSON (dumps = "dump to string")
json_data = json.dumps(data, indent=2)  # indent digunakan untuk format inden yang lebih baik

# Menulis JSON ke file
with open("data.json", "w") as file:
    file.write(json_data)

