import string 


pengamvilan = "halo kawan ku semua halo halo nya nama saya adalah mahdi"
countt = pengamvilan.count("halo")
print(countt)
pengambilan_1 = pengamvilan.capitalize()
print(pengambilan_1)


stinggg = "halomahdi99"
if stinggg.endswith("."):
    print("ya ini bisa di pakai ya")


string_dengan_tab = "Nama:\tAlice\tUsia:\t30"
menjadikan_spasi = string_dengan_tab.expandtabs()

# penggunaan is dalam strinfg
stingg = "halomahdi99"
isal = stingg.isalnum()
isalpa = stingg.isalpha()
isasciiii = stingg.isascii()
mengecek_spasi = stingg.isspace()   
mengecek_huruBesar = stingg.isidentifier()
print(f"identifier : {mengecek_huruBesar}")
print(f"mengecek spasi : {mengecek_spasi}")
print(f"mengecek asci : {isasciiii}")
print(f"mengecek huruf :{isalpa}")
print(f"mengecek string & angka : {isal}")

string_1 = "mahdisiji,aguagauga"
string_2 = "baso"
penggabungan_string = ",".join(" ")
print(string_1)


pengguna_replace = "aku akan menggunakan sebuah transmisi dan aku juga akan melawan"
pengguna_replace += pengguna_replace.replace("aku","saya", 4)
print(pengguna_replace)