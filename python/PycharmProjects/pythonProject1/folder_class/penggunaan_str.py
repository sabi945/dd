class Mahdi:
    def __init__(self, nama, usia):
        self.nama = nama 
        self.usai = usia
    def __str__(self):
        return f"nama : {self.nama} umur : {self.usai}"

baso = Mahdi("madun", 10)
print(str(baso))
