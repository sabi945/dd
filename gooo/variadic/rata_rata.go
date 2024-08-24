package main

import "fmt"

func menghitungRata(angka ...int) int{
	total := 0

	for _, args := range angka {
		total += args
	}

	rata := total / len(angka)
	return rata 
}

func main() {
	rata_rata := menghitungRata(10,20,30,40)
	fmt.Println("rata-ratanya :",rata_rata)

}