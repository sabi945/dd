class Mobil:
    def __init__(self,nama, warna):
        self.__nama = nama
        self.__warna = warna
    def get_nama(self):
        return self.__nama
    def get_warna(self):
        return self.__warna

    def set_nama(self, baso):
        self.__warna = baso

panggilan = Mobil("toyota", "hitam")
panggilan.set_nama("hijau")
print(f"jenis mobil : {panggilan.get_nama()} | warna : {panggilan.get_warna()}")
        