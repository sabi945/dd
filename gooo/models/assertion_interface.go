package main

import "fmt"

type Hewan interface {
	baso() string
}

type Manusia struct{
	nama string
}

func hasil(hewan Hewan)  {
	if kucing, ok := hewan.(Manusia); ok {
		fmt.Println(kucing)
	}
}