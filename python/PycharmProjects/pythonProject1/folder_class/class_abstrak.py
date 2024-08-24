from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, merk):
        self.merk = merk

    @abstractmethod
    def bergerak(self):
        pass

class Mobil(Kendaraan):
    def bergerak(self):
        return f"Mobil {self.merk} bergerak dengan roda."

class Motor(Kendaraan):
    def bergerak(self):
        return f"Motor {self.merk} bergerak dengan dua roda."

# Menghasilkan eror jika mencoba menginstansiasi kelas abstrak
# kendaraan1 = Kendaraan("Toyota")

# Membuat objek dari kelas turunan
mobil1 = Mobil("Toyota")
motor1 = Motor("Honda")

print(mobil1.bergerak())
print(motor1.bergerak())
