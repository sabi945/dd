import time
from datetime import datetime
import pytz
# waktu_makassar = time.localtime()
# pengambilan_makassar = time.asctime(waktu_makassar)
# print(pengambilan_makassar)

# def waktu_procesors():
#     waktu_cpu = time.process_time()
#     for _ in range(1000000):
#         pass
#     akhir_cpu = time.process_time()
#     print(f"waktunya : {waktu_cpu} : {akhir_cpu}")
# waktu_procesors()


# pengambilan_waktu = datetime.now()
# print(pengambilan_waktu.strftime("%Y/%m/%d, %H:%M"))

# mengambil_waktu_local = time.localtime()
# format_local = time.asctime(mengambil_waktu_local)
# print(format_local)

# waktu_timezone = time.time()
# haha = time.localtime(waktu_timezone)
# loacl = waktu_timezone.
# print(loacl)
# print(haha)
daylight_saving_active = time.daylight   # No parentheses needed
print(daylight_saving_active)