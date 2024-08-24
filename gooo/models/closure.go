package main

import "fmt"


func main(){
	clousures := 0

	hasil := func() {
		fmt.Println("hallo")
		clousures++
	}
	clousures++
	hasil()
	hasil()
	hasil()
	fmt.Println(clousures)

	

}