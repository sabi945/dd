package main

import "fmt"

func name(nama int) (int, string) {
	saso := "halo"
	return nama,saso
}
func main(){
	siji,result := name(1)
	fmt.Println("angka",siji)
	fmt.Println("pesan :",result)
}