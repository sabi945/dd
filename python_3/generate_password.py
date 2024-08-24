import timer
# import bcrypt

# def generate_password(inputt,password):
#     membuat_acak = bcrypt.gensalt()
#     ss = bcrypt.hashpw(password.encode("utf-8"),membuat_acak)
#     mengecek_password = bcrypt.checkpw(inputt.encode("utf-8"),ss)
#     if mengecek_password == True:
#         print(ss)



# buat_pasword = input("membuat password : ")
# baso = buat_pasword
# cek_password = input("masukkan password: ")

# panggilan= generate_password(cek_password,buat_pasword)

# import sched
# import time

# def backup():
#     print("Performing backup...")

# scheduler = sched.scheduler(time.time, time.sleep)

# # Menjadwalkan backup untuk dijalankan setiap 10 detik
# def schedule_backup():
#     scheduler.enter(10, 1, backup)
#     scheduler.enter(10, 1, schedule_backup)

# schedule_backup()
# scheduler.run()






# project kecil untuk sched

# import sched
# import time

# masukan = input("masukkan apa yang ada pesan")

# def print_messages():
#     print(f"pesanan telah jadi {masukan}")

# schedularr = sched.scheduler(time.time,time.sleep)

# print("tgg beberapa detik ya!")

# schedularr.enter(5,1,print_messages)

# schedularr.run()


import sched
import time
import itertools

# Membuat scheduler
scheduler = sched.scheduler(time.time, time.sleep)

def generate():
    