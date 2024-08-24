data = {}

while True:
    key = input("Masukkan kunci (atau ketik 'selesai' untuk berhenti): ")
    
    if key.lower() == 'selesai':
        break
    
    if key in data:
        print(f"Kunci '{key}' sudah ada dalam dictionary. Silakan masukkan kunci yang berbeda.")
        continue
    
    value = input(f"Masukkan nilai untuk kunci '{key}': ")
    
    # Mencoba untuk mengonversi nilai ke tipe data yang sesuai
    try:
        value = eval(value)
    except:
        pass  # Jika konversi gagal, biarkan nilai tetap sebagai string
    
    data[key] = value
    print(f"Data ditambahkan: {key} => {value}")
    print("Dictionary saat ini:", data)
    
print("Hasil akhir dari dictionary:", data)
