import readline
import os

def print_files_in_columns(file_list, column_width=20, num_columns=5):
    # Menentukan jumlah baris
    num_files = len(file_list)
    num_rows = (num_files + num_columns - 1) // num_columns  # Pembulatan ke atas
    
    # Membuat format string untuk setiap kolom
    col_format = "{:<" + str(column_width) + "}"
    
    for row in range(num_rows):
        row_files = []
        for col in range(num_columns):
            idx = row + col * num_rows
            if idx < num_files:
                row_files.append(col_format.format(file_list[idx]))
            else:
                row_files.append(col_format.format(""))
        print(" ".join(row_files))

while True:
    inputan = input("massukkan (ganti) : ") 
    if inputan == "ganti":
        pengganti = input("ganti apa : ")
    
    if inputan == "ls":
        hasil = os.listdir()
        print_files_in_columns(sorted(hasil))   
    if inputan == "q":
        break
