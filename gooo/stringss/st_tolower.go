package main

import (
	"fmt"
	"strings"
)


func main() {
	percobaan := "SEMUANYA ITU dunia dunia dunia"
	//percobaan replace
	old := "dunia"
	baru := "pemograman"
	hasi := strings.Replace(percobaan, old,baru,-1)
	fmt.Println(hasi)
	
	//percobaan Tolower 
	hasil := strings.ToLower(percobaan)
	fmt.Println(hasil)

	
}