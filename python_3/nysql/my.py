# Kompilasi kode sumber sebagai pernyataan
code_str = "print('Hello, world!')"
code_obj = compile(code_str, '<string>', 'exec')
exec(code_obj)

# Kompilasi kode sumber sebagai ekspresi
code_str = "3 + 5"
result = eval(code_str)
print(result)  # Output: 8


masukkan_ekspresi = input("masukkan ekspresi penjumlahan (misal: '3 + 5') : ")

# Evaluasi ekspresi
hasil = eval(masukkan_ekspresi)

print(f"Hasil evaluasi: {hasil}") 