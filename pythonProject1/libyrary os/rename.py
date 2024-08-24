import os

print("sebelum perubahan ", os.listdir())

ubah = os.rename("mahdi.txt", "mahd.txt")
print("perubahan yang di lakukan ", os.listdir())
