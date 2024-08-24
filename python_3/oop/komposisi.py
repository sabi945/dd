class Engine:
    def bass(self):
        return "engine start"
class Mobil:
    def __init__(self,name):
        self.name = name
        self.baso = Engine()
    def hasil(self):
        return self.baso.bass()   

hasil_nya = Mobil("toyota")
print(hasil_nya.hasil())