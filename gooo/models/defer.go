package main

import "fmt"

func satu() {
	fmt.Println("satu")
}
func dua(){
	fmt.Println("dua")
}
func tiga(){
	defer satu()
	fmt.Println("tiga")
	dua()

}

func main(){
	tiga()
}