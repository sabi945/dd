info = [1,2,3,4,5]
halo = ["siji","baso", "hasi", "sojo", "kijo", "baso"]
data = [1,8,4,2,6,1,4,7]
siji = info.insert(0, "halo")

menambah = info.append("siji")

hapus = info.remove("halo")

pop = info.pop(3)

mengambil = info.index(3)

menghitung_panjang = len(info)

mengambil_data_sesuai_dari_index_berapa_ke_berapa = info[1:4]

zipp = zip(info, halo)
for i, ji in zipp:
    print(f"{i} {ji}")

so = data.sorted()

print(so)
print(zipp.__dir__)
print(f"mengambil data dari index satu sampai ke 4 : {mengambil_data_sesuai_dari_index_berapa_ke_berapa}")
print(f"menghitung panjang list : {menghitung_panjang}")
print(f"mengambil nilai sesuai index yang di tentukan : {mengambil}")
print(info)
print(f"pop : {pop}")