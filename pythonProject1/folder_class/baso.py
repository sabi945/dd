# class bas:
#     def __init__(self, baso):
#         self.baso = baso
#     def __getitem__(self, index):
#         return self.baso[index]
#     def __setitem__(self, siji, halo):
#         self.baso[siji] = halo

# b = bas([1,2,3,4,5])
# b[2] = 8
# print(b[2])

kumpulan = [1,2,3,4,5]
siji = "baso"
c = "b" in siji
print(c)

ss = "baso"
halo = "baso"
a = ss is halo
print(a)
