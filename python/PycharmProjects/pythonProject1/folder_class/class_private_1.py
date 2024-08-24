class Baso:
    def __init__(self,nama,health):
        self.__name = nama
        self.__kelas = health
    def getNama(self):
        return self.__name
    def getHealth(self):
        return self.__kelas
    def serang(self,attack):
        self.__kelas -= attack

baso = Baso("mahdi",20)

print(baso.getNama())
baso.serang(5)
print(baso.getHealth())