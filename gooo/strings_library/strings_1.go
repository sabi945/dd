package main

import (
	"fmt"
	"strings"
)

func main(){
	// untuk mengecek apakah variavbel copy berisi di depan said
	said := "Hallo World"
	copy := "Hallo"
	fmt.Println(strings.HasPrefix(said,copy))

	//sama dengan di atas tapi yang ini paling akhir
	copy_1 := "World"
	fmt.Println(strings.HasSuffix(said,copy_1))

	//untuk melihat apakah hal yang di tuliskan ada di object yang di tuju
	copy_2 := "H"
	fmt.Println(strings.Contains(said,copy_2))

	//untuk mengganti satu kata atau lebih
	copy_3 := "World"
	fmt.Println(strings.Replace(said,copy_3,"baso",1))

	//
	fmt.Println(strings.ToUpper(said))
	fmt.Println(strings.ToLower(said))


	
}