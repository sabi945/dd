package main

import (
	"fmt"
	"strings"
)

func main(){
	percobaan := "halo dunia"

	hasil_percobaan := strings.Contains(percobaan,"du")

	if hasil_percobaan {
		fmt.Println("hasil sudah di temukan")
	} else {
		fmt.Println("data tidak di temukan")
	}
}