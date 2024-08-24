package main

import "fmt"
func pertama(name bool) {
	if name == false {
		panic("ups ada ke salahan")
	}
	fmt.Println("selesai")
}

func kedua() {
	er := recover()
	if er != nil {
		fmt.Println("kesalahan :",er)
	}
	fmt.Println("selesai")
}

func main(){
	pertama(false)
	defer kedua()
}