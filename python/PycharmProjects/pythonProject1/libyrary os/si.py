import psutil

# Mendapatkan daftar proses yang sedang berjalan
processes = psutil.process_iter()

# Mencetak informasi tentang proses pertama
process = next(processes)
print(process.name, process.pid, process.cpu_percent())
