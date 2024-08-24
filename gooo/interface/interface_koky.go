package main

import "fmt"

type pemasak interface {
	cocy() string
}

type ayam struct{}

func (a ayam) cocy() {
	fmt.Println("ayam kcf")
}
func pesanan(b pemasak,vehicle string) {
	fmt.Println("masakan",vehicle)
}
func main() {
	pemanggilan := ayam{}

	pesanan(pemanggilan,"ready")
}
