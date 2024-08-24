package main

import "fmt"

// Interface
type Hewan interface {
	Suara() string
}

// Implementasi interface untuk kucing
type Kucing struct{}

func (k Kucing) Suara() string {
	return "Meow!"
}

// Implementasi interface untuk anjing
type Anjing struct{}

func (a Anjing) Suara() string {
	return "Guk guk!"
}

// Fungsi yang menggunakan interface
func InteraksiHewan(h Hewan) {
	fmt.Println("Hewan tersebut bersuara:", h.Suara())
}


func main() {
	// Membuat objek Kucing
	kucing := Kucing{}
	// Membuat objek Anjing
	anjing := Anjing{}

	// Menggunakan fungsi yang menerima interface
	InteraksiHewan(kucing) // Output: Hewan tersebut bersuara: Meow!
	InteraksiHewan(anjing) // Output: Hewan tersebut bersuara: Guk guk!

}
