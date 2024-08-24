package main

import "fmt"

type Manusia struct {
	nama string
	umur int
}

type embedding struct {
	Manusia
	nim int
}

func main() {
	pemanggilan := embedding{
		Manusia: Manusia{"mahdi",10},
		nim: 100,
	}

	fmt.Println(pemanggilan.nim)
	fmt.Println(pemanggilan.nama)
}
