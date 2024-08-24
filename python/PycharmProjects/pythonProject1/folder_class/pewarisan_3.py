class Kendaraan:
    def __init__(self, nama,merek):
        self.nama = nama
        self.merek = merek
    def hasil(self):
        return f"{self.nama}{self.merek}"
class Mobil(Kendaraan):
    def __init__(self,nama,merek,roda):
        super().__init__(nama, merek)
        self.roda = roda
    def hasil(self):
        return f"ini adalah mobil {super().hasil()} beroda {self.roda}"
    def __str__(self):
        return self.hasil()
kendaraan = Mobil("honda ","civik",4)
print(kendaraan)

