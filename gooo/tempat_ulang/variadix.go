package main

import "fmt"

func nama(name ...int) int {
	total := 0
	for _,siji := range name {
		total += siji
	}
	return total
}

func main() {
	baso := nama
	result := []int{10,10,10,10,10}
	fmt.Println(baso(result...))
}