package main

import "fmt"

type Loop interface {
	ulangan() int
}

type ikutan_loop struct{}

func (h ikutan_loop) ulangan() string {
	for hasil := 0; hasil < 5; hasil++ {
		fmt.Println(hasil)
	}
	return "selesai"
}


func main() {
	perulangan := ikutan_loop{}

fmt.Println(perulangan.ulangan())
}