class Mobil:
    def __init__(self, merek, tahun):
        self._merek = merek  # Atribut "private" dengan awalan _
        self._tahun = tahun

    # Getter untuk merek
    @property
    def merek(self):
        return self._merek

    # Setter untuk merek
    @merek.setter
    def merek(self, value):
        if value and isinstance(value, str):
            self._merek = value
        else:
            print("Merek harus berupa string dan tidak boleh kosong")

    def info_mobil(self):
        return f"Mobil {self._merek} tahun {self._tahun}"

mobil = Mobil("Honda", 2022)

# Menggunakan getter (properti) untuk mengambil merek
merek = mobil.merek
print(f"Merek mobil: {merek}")

# Menggunakan setter (properti) untuk mengubah merek
mobil.mere = "Toyota"

# Menggunakan getter lagi untuk memeriksa perubahan
merek = mobil.merek
print(f"Merek mobil setelah perubahan: {merek}")
