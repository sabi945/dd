import bcrypt as bc

def has_password(password):
    simpan = bc.gensalt()
    hasing = bc.hashpw(password.encode('utf-8'),simpan)
    return hasing
def salt_password(password, hashed):
    return bc.checkpw(password.encode('utf-8'),hashed)

inputan = input("password baru : ")
hasnya = has_password(inputan)
print(f"format nya : {hasnya}")

inputt = input("verivikasi : ")
if bc.checkpw(inputt.encode('utf-8'),hasnya):
    print("selamat anda sudah membuat sebuah password")
else:
    print("upss anda salah!")


