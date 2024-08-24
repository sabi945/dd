class Kendaraan:
    def __init__(self, merek, model):
        self.mere = merek
        self.mode = model

    def info(self):
        return f"{self.mere} {self.mode}"


# Kelas Anak Pertama (Subclass)
class Mobil(Kendaraan):
    def __init__(self, mer, mod, roda):
        super().__init__(mer, mod)  # Memanggil konstruktor kelas induk
        self.jumlah_roda = roda

    def info(self):
        return f"Mobil {super().info()}, {self.jumlah_roda} roda"


# Kelas Anak Kedua (Subclass)
class SepedaMotor(Kendaraan):
    def __init__(self, merek, model, mesin):
        super().__init__(merek, model)
        self.tipe_mesin = mesin

    def info(self):
        return f"Sepeda Motor {super().info()}, mesin {self.tipe_mesin}"


# Membuat Objek Kelas Anak
sedan = Mobil("Toyota", "Camry", 4)
motor = SepedaMotor("Honda", "CBR 250", "4-tak")

# Mengakses metode info() dari kelas anak
print(sedan.info())
print(motor.info())
