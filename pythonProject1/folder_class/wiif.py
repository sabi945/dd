import wifi_2
import fire

def baso(parameter):
    buatan = wifi_2.hasil(parameter)
    return buatan
inputan = input("masukkan nama : ")
print("-----hasil-----")
panggilan = baso(inputan)
print(panggilan)