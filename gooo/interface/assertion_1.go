package main

import "fmt"

func main() {
	var baso interface{} = "hallo"

	i := baso.(string)
	fmt.Println(i)

	bass, ok := baso.(float64)
	if !ok {
		fmt.Println("hasil nya sudah benar")
	} else {
		fmt.Println(bass)
	}

	var bas int = 10
	perubahan := float32(bas)
	fmt.Println(perubahan)
}
