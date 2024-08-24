package main

import (
	"fmt"

)


func percobaan(arr []int) {
	fmt.Println("looping nya ada di bawah kawan ku")
	for _, vle := range arr {
		fmt.Println(vle)

	}
}

func main() {
	myarray := []int{1,2,3,4,5,7,8,9}

	percobaan(myarray)


	my_baso := [...]int{1,2,3,4,5,6,7,8,9,0,0,0,0}
	fmt.Println(my_baso)	
}