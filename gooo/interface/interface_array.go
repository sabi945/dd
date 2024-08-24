package main

import "fmt"

type Animal interface {
	Suara() string
}

type Dog struct {
}

func (a Dog) Suara() string {
	return "guk guk"
}
type cat struct {

}

func (b cat) Suara() string {
	return "meow"
}


func main() {
	pemanggilan := cat{}
	fmt.Println(pemanggilan.Suara())
}
