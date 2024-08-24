class Mobil:
    def __init__(self, merek, model, roda):
        self.merek = merek
        self.model = model
        self.roda = roda
    def info(self):
        return f"{self.merek} {self.model} {self.roda}"

obejct = Mobil("toyota","sedan",9)
print(obejct.info())

