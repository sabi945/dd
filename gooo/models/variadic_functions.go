package main

import "fmt"

func baso(number ...int) int {
 total := 0
	for _, numbe := range number {
		total += numbe
	}
 return total
}


func main() {
	result := baso(10,3,10)
	fmt.Println(result)

	repuk := []int{10,10,10,10}
	fmt.Println(baso(repuk...))

}