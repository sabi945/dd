
data = []


while True:
    inputan = input("masukkan inputan : ")

    # menghapus inputan
    if inputan.lower() == "remove":
        baso = input("masukkan data yang ingin di hapus : ")
        if baso in data:
            data.remove(baso)
            print("data telah di hapus")
        else:
            print(f"ups data {baso} tidak ada dalam database")
    # membuat berhenti proses
    if inputan.lower() == "selesai":
        break

    # melihat data 
    if inputan.lower() == "ck":
        for bas in data:
            print("- ",bas)
        continue

    # menghapus semua data data
    if inputan.lower() == "hapus":
        data.clear()
        print("semua data telah di hapus")
        continue

    # menambahkan data
    if inputan == "tambah":
        while True:
            basi = input("masukkan input add : ")
            data.append(basi)
            print(f"{inputan} di tambahkan ke database ")

            if basi == "exit":
                break
    

print("hasil dari data yang sudah di input")
for baso in data:
    print("- ",baso)