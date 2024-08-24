package main

import (
	"bufio"
	"fmt"
	"os"
)
func main(){
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("masukkan nama anda : ")
	scanner.Scan()
	pengambilan_scanner := scanner.Text()		
	fmt.Print("masukkan angka : ")
	scanner.Scan()
	pemgambilan := scanner.Text()
	fmt.Print("hasil : ", pengambilan_scanner,"\n")
	fmt.Println("hasl dari int : ", pemgambilan)

	
		
	

}
