# class Gettitem:
#     def __init__(self, indeks):
#         self.indeks = indeks
#     def __getitem__(self, angka):
#         return self.indeks[angka]

# baso = Gettitem([1,2,3,4,5])
# print(baso[2])

class Mlist:
    def __init__(self):
        self.nama = []
    def akses(self):
        return self.nama
    def akses_2(self, index):
        self.nama = index

    def ada(self, elemen):
        self.nama.append(elemen)

# Membuat objek dari kelas Mlist
baso = Mlist()
masuk = True
while (masuk):
    inputan = input("Masukkan nama input : ")
    baso.ada(inputan)
    
    
    if inputan.lower() == "masu":
        sij = True
        while(sij):
            masukan = input("masukkan input : ")
            if masukan in baso.akses():
                print(f"ini adalah hasil nya : {masukan}")
            elif masukan == "exit":
                sij = False
            else:
                print("masukkan inputan yang benar!")



    


