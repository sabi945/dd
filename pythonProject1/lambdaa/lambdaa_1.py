def pemanggil(hasil):
    def tambah(a,y):
        return a + y
    def kurang(b,t):
        return b - t
    
    if hasil == "tambah":
        return tambah
    elif hasil == "kurang":
        return kurang
    
inputan = str(input("masukkan operator : "))
pemanggilan = pemanggil(inputan)
masukan_1 = int(input("masukkan angka pertama : "))
masukan_2 = int(input("masukkan angka ke dua : "))
print(pemanggilan(masukan_1,masukan_2))
