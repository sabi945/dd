import subprocess
import time

def get_cpu_temp():
    try:
        # Jalankan perintah osx-cpu-temp dan tangkap outputnya
        result = subprocess.run(['osx-cpu-temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise Exception(f"Error running osx-cpu-temp: {result.stderr.decode('utf-8').strip()}")
        temp = result.stdout.decode('utf-8').strip()
        return temp
    except FileNotFoundError:
        return "osx-cpu-temp not found. Please ensure it is installed and in your PATH."

def display_cpu_temp(interval=5):
    try:
        while True:
            cpu_temp = get_cpu_temp()
            print(f'Suhu CPU saat ini: {cpu_temp}')
            time.sleep(interval)  # Jeda waktu dalam detik
    except KeyboardInterrupt: 
        print("Monitoring dihentikan oleh pengguna.")

if __name__ == '__main__':
    display_cpu_temp(2)  # Menampilkan suhu CPU setiap 5 detik

# import subprocess

# result = subprocess.run(['grep', 'pattern'], input='This is a sample text', stdout=subprocess.PIPE, text=True)
# print(result)