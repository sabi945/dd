import random

data = [
    "Hidup itu seperti pisang goreng, kadang manis, kadang gosong, tapi yang penting jangan sampai basi.",
    "Aku bukan pemalas, aku cuma sedang menjalankan mode hemat energi.",
"Kalau saja mulutmu punya BPKB, pasti sudah aku gadaikan.",
"Jangan sombong kalau jadi atasan, di rumah juga masih disuruh cuci piring.",
"Aku tidak sedang menghinamu, aku sedang mendeskripsikanmu secara jujur.",
"Punggungku bukan voice-mail, jadi jangan curhat di belakangku.",
"Kalau zombie menyerbu, kamu bakal aman. Soalnya mereka cuma makan otak.",
"Aku terjebak antara Aku harus nabung dan YOLO (You Only Live Once)",
"Bukannya anti sosial, aku cuma selektif dalam bersosial.",
"Motivator dan pembicara tak dapat membuatku rajin bekerja. Kecuali bosku yang bilang, Gajimu naik!"
]
while True:
    key = input("masukkan keyword nya : ")
    if key == "kata":
        hasil = random.choice(data)
        print(hasil)
    if key == "exit":
        break
