import re

# Tentukan pola regular expression
# pattern = r'world'

# # String yang ingin Anda uji cocokkan
# string = 'hello world'

# # Memanggil method match()
# match = re.search(pattern, string)

# # Periksa apakah ada kecocokan
# if match:
#     print("Pola ditemukan di awal string")
#     print(f"tempat strin {match.start()}")
# else:
#     print("Pola tidak ditemukan di awal string")

# patternn = r''

# # String yang ingin Anda uji cocokkan
# stringg = 'word'

# # Memanggil method match()
# matchh = re.findall(patternn, stringg)


# if matchh:
#     print(matchh)
# else:
#     print("salah guys")

pattern = r'\s+'  # Ini adalah pola untuk mencocokkan satu atau lebih spasi putih

# String yang ingin Anda pecah
string = 'hello world example mahdi'


# Memisahkan string menggunakan re.split()
result = re.split(pattern, string)

# Cetak hasil pemisahan
print("Hasil pemisahan:", result)