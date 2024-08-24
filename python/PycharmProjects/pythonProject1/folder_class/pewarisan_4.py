class Kendaraan:
    def __init__(self,nama, merek):
        self.nama = nama
        self.merek = merek
    def eksekusi(self):
        return f"nama : {self.nama} merek : {self.merek}"

class Mobil(Kendaraan):
    def __init__(self, nama, merek, mesin):
        self.mesin = mesin
        super().__init__(nama, merek)
    def baso(self):
        return f"{super().eksekusi()} mesin : {self.mesin}"

baso = Mobil("mobil", "thamry", "jadul")
print(baso.baso())
