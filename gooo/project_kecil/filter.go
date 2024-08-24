package main

import "fmt"

func anjing() string {
	return "anjing"
}


func filterr(nama string) {
	if nama == "anjing" {
		fmt.Println("ini hal yang kasar")
	}
}

func main() {
	filterr(anjing())
}