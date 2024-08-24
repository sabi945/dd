import shutil
import time

def display_progress_bar(progress, total):
    size = shutil.get_terminal_size()
    columns = size.columns
    bar_length = columns - 30  # Panjang progress bar, disesuaikan dengan lebar terminal
    
    filled_length = int(bar_length * progress // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    
    print(f'\rProgress: |{bar}| {progress}/{total}', end='')

total = 100
for i in range(total + 1):
    display_progress_bar(i, total)
    time.sleep(0.1)
print()  # Untuk memulai baris baru setelah progress bar selesai
