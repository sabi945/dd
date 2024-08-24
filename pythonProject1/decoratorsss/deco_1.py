# Decorator Riski
def riski_decorator(fungsi):
    
    print("Riski melakukan sesuatu sebelum fungsi dijalankan")
    fungsi()
    

    return riski_decorator

# Fungsi Mahdi dengan decorator Riski
@riski_decorator
def mahdi():
    print("Fungsi Mahdi dijalankan")

# Fungsi Riski dengan decorator Riski


# Memanggil fungsi Mahdi
mahdi()