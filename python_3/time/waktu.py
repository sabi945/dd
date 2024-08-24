import time

# Menggunakan perf_counter untuk pengukuran waktu dengan akurasi tinggi
# start_perf = time.perf_counter()
# time.sleep(1)
# end_perf = time.perf_counter()
# print(f"Elapsed time using perf_counter: {end_perf - start_perf} seconds")

# # Menggunakan process_time untuk mengukur waktu CPU yang digunakan oleh proses saat ini
# start_cpu = time.process_time()
# # Blok kode yang ingin diukur
# end_cpu = time.process_time()
# print(f"CPU time used: {end_cpu - start_cpu} seconds")
for baso in range(4):
    print(baso)
    if baso == 3:
        time.sleep(3)