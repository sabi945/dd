class Baso:
    def __init__(self,nama,hewan):
        self.name = nama
        self.hewan = hewan
    def suara(self):
        print(f"{self.name} is woriking to {self.hewan}")

class Orang(Baso):
    def __init__(self,name ,kerjaan):
        super().__init__(name,kerjaan)
    def suara(self):
        super().suara()

panggilan = Baso("sabi","kucing")
panggilan_1 = Orang("mahdi","bca")
panggilan_1.suara()
panggilan.suara()