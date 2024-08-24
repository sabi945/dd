package main

import "fmt"

func main(){
	var baso = [...]int {1,2,10,4,5}
	for i := 0; i < len(baso); i++   {
		fmt.Println("hallo", i)

	}
	tampungan := baso[:3]
	fmt.Println(tampungan)


}