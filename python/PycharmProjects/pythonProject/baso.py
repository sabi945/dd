import datetime as dt
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)