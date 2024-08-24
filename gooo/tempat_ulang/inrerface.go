package main

import "fmt"

type Hewan interface {
	Suara() string
}

type Kucing struct {
	kucing_1 string
}

func (a Kucing) Hewan()  {
	for baso, _:= range a.kucing_1 {
		fmt.Println(baso)
	}
}

func maian() {
	bass := Kucing{kucing_1: "mahdi"}
	var basi Hewan()
	basi = bass
}