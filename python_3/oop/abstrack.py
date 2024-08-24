from abc import ABC ,abstractmethod
class Teh(ABC):
    def __init__(self, nama):
        self.nama = nama
    @abstractmethod
    def baso(self):
        pass
class tehAbc(Teh):
    def baso(self):
        print(f"hallo apa kabar {self.nama}")

panggil = tehAbc("baso")
panggil_1 = Teh("basi")
panggil_1.baso()
panggil.baso()