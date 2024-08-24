with open('project.py') as f:
    total_length = sum(len(line) for line in f)  # Menjumlahkan panjang setiap baris dalam file
    print(total_length)
