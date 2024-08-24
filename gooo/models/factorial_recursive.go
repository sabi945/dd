package main

import "fmt"

func reecursive(value int ) (int){
	if value == 1 {
		return 1
	} else {
		return value * reecursive(value-1)
	}
}
func main() {
	fmt.Println(reecursive(10))
	fmt.Println(1*2*3*4*5*6*7*8*9*10)

}