package main

import "fmt"

// Definisikan sebuah interface untuk stasiun pengisian bahan bakar
type GasStation interface {
    FillGas() string
}

// Implementasi untuk mobil konvensional
type Sedan struct{}

// Metode untuk mengisi bensin pada mobil konvensional
func (s Sedan) FillGas() string {
    return "ayam kfc"
}

// Implementasi untuk truk
type Truck struct{}

// Metode untuk mengisi bensin pada truk
func (t Truck) FillGas() string {
    return "Mengisi bensin pada truk."
}

// Implementasi untuk mobil listrik
type ElectricCar struct{}

// Metode untuk mengisi daya pada mobil listrik
func (e ElectricCar) FillGas() string {
    return "Mengisi daya pada mobil listrik."
}

// Fungsi untuk mengisi bahan bakar di stasiun pengisian
func FuelUp(station GasStation, vehicle string) {
    fmt.Println(station.FillGas(), vehicle)
    
}

func main() {
    // Membuat instance dari berbagai jenis kendaraan
    sedan := Sedan{}
	FuelUp(sedan,"ready")
   
}
 