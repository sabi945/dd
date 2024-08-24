class INDUK:
    def __init__(self, nama, makanan):
        self.nama = nama
        self.makanan = makanan
class sapi(INDUK):
    def __init__(self, nama, makanan):
        super().__init__(nama,makanan)

herbivora = sapi("sapi", "rumput")

inputan = input("masukkan nama makanan : ")

if inputan == "rumput":
    print(f"{herbivora.nama} adalah pemakan herbivora")
else:
    print("masukkan inputan yang benar")