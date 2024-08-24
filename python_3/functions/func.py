# def baso(*siji):
#     for haha in siji:
#         print(haha)

# baso(1,"baso", 3,5,6,5)

# def basi(**halo):
#     for var, siji in halo.items():
#         print(f"{var}: {siji}")
 
# basii = 10
# hasim = 20
# basi(basii=80,hasim=hasim)

import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
    
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Pengguna menentukan password
password = input("Masukkan password yang ingin Anda gunakan: ")
hashed_password = hash_password(password)
print(f"Password: {password}")  
print(f"Hashed: {hashed_password}")

# Verifikasi password
input_password = input("Masukkan password untuk verifikasi: ")
if check_password(input_password, hashed_password):
    print("Password cocok")
else:
    print("Password tidak cocok")
