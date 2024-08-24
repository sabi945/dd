package main

import "fmt"

func main(){

	// // untuk float %f
	// result := 170.32
	// fmt.Printf("angka : %.5f\n", result)

	// // untuk int
	// umur := 10
	// fmt.Printf("umur : %d\n", umur)

	// //untuk string
	// nama := "mahdi"
	// fmt.Printf("nama : %s\n",nama)

	// // untuk boolean
	// berhasil := true
	// fmt.Printf("hasil : %t", berhasil)


	// number := 255
    // // %x: heksadesimal dalam huruf kecil
    // fmt.Printf("Decimal: %d, Hexadecimal (lowercase): %x\n", number, number)

	// //menampilkan alamat memori
	// numbe := 12
	// point := &numbe
	// fmt.Printf("value : %d\npoint : %p", numbe, point)

	//penggunaan built in function fmt
	nama_1 := "baso"
	umurr := 10
	penampungan := fmt.Sprintf("nama : %s\numur : %d",nama_1, umurr)
	fmt.Println(penampungan)



	// Contoh string yang akan di-parse
	inputString := "John 30 10"
	// Deklarasi variabel untuk menyimpan jumlah elemen yang berhasil diparse
	var parsedCount int

	// Deklarasi variabel untuk menyimpan hasil parsing
	var name string
	var age int
	var ini int

	// Menggunakan Sscanf untuk mem-parse string
	parsedCount, err := fmt.Sscanf(inputString, "%s %d %d", &name, &age, &ini)

	// Memeriksa kesalahan selama parsing
	if err != nil {
		fmt.Println("Error:", err)
	}

	// Menampilkan hasil parsing dan jumlah elemen yang berhasil diparse
	fmt.Printf("Name: %s\nAge: %d\nint_2 : %d\nParsed Count: %d\n", name, age,ini, parsedCount)
}


