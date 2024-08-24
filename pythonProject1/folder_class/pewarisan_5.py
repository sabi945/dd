class kendaraan:
    def __init__(self,mahdi,baso):
        self.mahdi = mahdi
        self.baso = baso
    def ifo(self):
        return f"{self.mahdi} {self.baso}"

pemanggilan = kendaraan("mahdi",10)
print(pemanggilan.ifo())