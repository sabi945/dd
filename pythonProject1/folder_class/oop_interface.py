from abc import ABC, abstractmethod

# Antarmuka untuk kendaraan
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def honk(self):
        pass

# Implementasi antarmuka untuk mobil
class Car(Vehicle):

    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

    def honk(self):
        print("Honk! Honk!")

# Implementasi antarmuka untuk sepeda
class Bicycle(Vehicle):

    def start_engine(self):
        print("Bicycle doesn't have an engine")

    def stop_engine(self):
        print("Bicycle doesn't have an engine to stop")

    def honk(self):
        print("Bicycle bell rings")

# Fungsi untuk berinteraksi dengan kendaraan
def interact_with_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.honk()
    vehicle.stop_engine()

# Contoh penggunaan
car = Car()
bicycle = Bicycle()

print("Interacting with a Car:")
interact_with_vehicle(car)

print("\nInteracting with a Bicycle:")
interact_with_vehicle(bicycle)
