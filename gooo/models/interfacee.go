package main

import "fmt"



type Hewan interface {
	jalan() string
	bangunan() string
}

type pembuat struct {
	nama string
}


func (a pembuat) bangunan() string {
	return fmt.Sprintln("pembat dari bangunan adalah",a.nama)
	
}

func main(){
	pengambilan := pembuat{
		nama: "mahdi",
	}
	fmt.Println(pengambilan.bangunan())
}