package main

import "fmt"

func baso(){
	fmt.Println("halo semuanya")
}
func main(){
	defer baso()
	
	fmt.Println("ohh ini berarti tidak bisa di eksekusi")
	panic("ada keslahan!")
	


}