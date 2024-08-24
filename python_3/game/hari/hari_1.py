import datetime as dt

def waktu():
    ob = dt.datetime.now()
    def tahun():
        hari_ini = ob.year
        print("tahun saat ini :", hari_ini)
    def waktu_saat_ini():
        waktu_ini = ob.time()
        print("waktu saat ini ", waktu_ini)
    return tahun,waktu_saat_ini

tahun, waktu_ini  = waktu()
inputan = input("masukkan apa yang anda ingin kan : ")
if inputan == "tahun":
    tahun()
elif inputan == "waktu":
    waktu_ini()