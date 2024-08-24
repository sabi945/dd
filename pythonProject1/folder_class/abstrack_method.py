from abc import ABC, abstractmethod
# class hewan:
#     @abstractmethod
#     def pernfasan(self):
#         pass 
# class anjing(hewan):
#     def pernafasan(self):
#         return f"gog gog"
# class kucing(hewan):
#     def pernafasan(self):
#         return "meong "
# def pengambilan(baso):
#     return baso.pernafasan()

# baso = anjing()
# siji = kucing()

# print(pengambilan(anjing()))

class Hewan:

    @abstractmethod
    def suara(self):
        pass
class Anjing(Hewan):
    def suara(self):
        print("guk guk")
class kucing(Hewan):
    def suara(sel):
        print("meong")
class pengambilan(Anjing,kucing):
    def suara_kucing(self):
        kucing.suara(self)

ambil = pengambilan()
ambil.suara(Anjing)


        

