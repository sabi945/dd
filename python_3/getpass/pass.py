import getpass
import g
def kunci():
    inputan = input("masukkan user : ")
    password = getpass.getpass("masukkan sandi anda : ")

    if inputan ==  "mahdi" and password == "admin123":
        print("login berhasil")
    else:
        print("anda salah input!")
if __name__ == "__main__":
    kunci()