package main

import (
	"fmt"

)

func printmessage(nama string,args interface{} ){
	message := fmt.Sprintf(nama, args)
	fmt.Println(message)
}

func main(){
	printmessage("halo %s", "mahdi")
}