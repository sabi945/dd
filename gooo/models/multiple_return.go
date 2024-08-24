package main

import "fmt"


func baso() (string,string,string) {
	mahdi := "mahdi"
	baso := "baso"
	siji := "siji"
	return mahdi,baso,siji
}

func main(){
	pemanggil,hai, kobi := baso()
	fmt.Println(pemanggil,hai,kobi)
}