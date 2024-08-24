package main

import "fmt"

func main(){
	multi_map := map[string]int{
		"nama" : 2,
		"kelas": 3,
	}
	multi_map["nama"] = 10
	fmt.Println(multi_map)
	fmt.Println(multi_map["party"])
	

}