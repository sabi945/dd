package main

import (
	"errors"
	"fmt"
)

func eror(halo, baso int) (int, error) {
	if baso > halo {
		return 0, errors.New("tidak bisa di bagia dengan nilai besar di akhir")
	} else {
		return halo / baso, nil
	}
}

func main(){
	ran, err := eror(8,10)
	if err != nil {
		fmt.Println("Erors :", err)
	} else {
		fmt.Println("hasil pembagian :", ran)
	}



}