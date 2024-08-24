package main

import "fmt"


func latihan(baso ...int) {
	for _, value := range baso {
	fmt.Println("hasil dari loop :", value)
	fmt.println("hasilnya adalah ini hehehehe")
	}
}
func main() {
	array := []int{1,2,3,4,5,6,}
	latihan(array...)
	baba
}
