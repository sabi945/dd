# class Hewan:
#     def suara(self):
#         print("suaranya")
# class Kucing:
#     def suara(self):
#         print("meow")
# def pewarisan(Hewan):
#     return Hewan.suara
# panggilan = Kucing()
# hasil = pewarisan(panggilan)
# hasil()

# calculator

# class Tambah:
#     def tambah(self,x,y):
#         return x + y
# class Kali:
#     def tambah(self,x,y):
#         return x * y
# def pengambilan(korup,x,y):
#     hasil = korup(x,y)
#     print(hasil)
# kali = Kali()
# pengambilan(kali.tambah,10,9)

class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        return "Suara hewan"

class Kucing(Hewan):
    def __init__(self, nama):
        super().__init__(nama)
    def bersuara(self):
        suara_induk = super().bersuara() # Menggunakan hasil dari metode induk
        return f"{suara_induk} {self.nama}, tapi lebih spesifik: Meong!"


kucing = Kucing("kucing")
print(kucing.bersuara())      # Output: "Suara hewan, tapi lebih spesifik: Meong!"


