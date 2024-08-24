package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main(){
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("masukkan nama anda : ")
	scanner.Scan()
	pengambilan := scanner.Text()
	fmt.Print("masukkan angka ke dua :")
	scanner.Scan()
	pengamnbilan_2 := scanner.Text()

	konversi_1,_ := strconv.ParseFloat(pengambilan,64)
	konversi_2,_ := strconv.ParseFloat(pengamnbilan_2, 64)
	
	penambahan := konversi_1 + konversi_2
	fmt.Println(penambahan)




}