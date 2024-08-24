import os
import psutil
import subprocess

# Fungsi untuk membersihkan file sementara
def bersihkan_cache():
    cache_dirs = [
        "~/Library/Caches/",
        "/Library/Caches/"
    ]
    
    for cache_dir in cache_dirs:
        os.system(f'rm -rf {cache_dir}*')
    print("Cache dibersihkan.")

# Fungsi untuk memantau dan menghentikan proses yang menggunakan terlalu banyak CPU
def hentikan_proses_berat(threshold=80):
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if proc.info['cpu_percent'] > threshold:
                print(f"Proses {proc.info['name']} (PID: {proc.info['pid']}) dihentikan karena penggunaan CPU yang tinggi.")
                os.kill(proc.info['pid'], 9)  # Menggunakan kill untuk menghentikan proses
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Fungsi untuk memantau penggunaan memori
def monitor_memori(threshold=80):
    memory_info = psutil.virtual_memory()
    if memory_info.percent > threshold:
        print(f"Peringatan: Penggunaan memori tinggi - {memory_info.percent}% digunakan.")

# Fungsi untuk mengatur prioritas proses Python sendiri
def atur_prioritas():
    pid = os.getpid()
    # Mengatur prioritas menjadi tinggi
    subprocess.run(["renice", "-n", "-20", "-p", str(pid)], check=True)
    print(f"Prioritas proses dengan PID {pid} diatur menjadi tinggi.")

# Jalankan fungsi-fungsi tersebut
if __name__ == "__main__":
    atur_prioritas()
    bersihkan_cache()
    hentikan_proses_berat()
    monitor_memori()
