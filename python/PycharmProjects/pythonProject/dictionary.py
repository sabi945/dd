my_dict = {
    "nama": "John Doe",
    "usia": 30,
    "alamat": "Jl. Merdeka No. 100, Jakarta"
}
# # metode dict.fromkeys
datat = {'a', 'b', 'c'}

penggunaaan = dict.fromkeys(datat,1)
print(penggunaaan)
print(datat)

for siji in my_dict.keys():
    print(siji)

halo = my_dict.popitem()
print(halo)
print(my_dict)

default = my_dict.setdefault("nama", "nama tidak di ketahui")
print(default)


# # metode update
# # cara untuk menambah kunci dan value baru
# baso = my_dict.update({"kelas": 10})
# # cara untuk mengganti isi dari sebuah kunci
# siji = my_dict.update({"nama": "baso"})
# print(my_dict)




# # metode get
# baso = my_dict.get("nama")
# print(baso)



# # metode pop
# baso = my_dict.pop("usia")
# print(baso)
# print(my_dict)



# # metode get default
# nilai_y = my_dict.get('y', 'Kunci tidak ditemukan')
# print(nilai_y)



# # metode items
# itemss = my_dict.items()
#
# for kunci in itemss:
#     print(f"kunci : {kunci}")



# # cara mengakses dictionary dengan langsung kunci and value
# for baso, siji in my_dict.items():
#     print(f'{baso} : {siji}')



# # cara mengakses dictionary 1
# kunci_1 = "nama"
# kunci_2 = "usia"
#
# for key, valu in my_dict.items():
#     if key == kunci_1 or key == kunci_2:
#         print(valu)


