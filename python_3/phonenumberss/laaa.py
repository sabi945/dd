import phonenumbers

# Kode negara yang ingin Anda cari kode wilayahnya
country_code = 62  # Misalnya, kode negara Bosnia dan Herzegovina

# Menggunakan metode country_code_for_region untuk mendapatkan kode wilayah
region_codes = phonenumbers.region_codes_for_country_code(country_code)

# Output daftar kode wilayah
print(f"Kode wilayah untuk negara dengan kode {country_code}: {region_codes}")
