package main

import "fmt"

func ano(name int,  fungsi func(int) int) int {
	result := fungsi(name)
	fmt.Println("hasil", result)
	return result
}
func tambah(a int) int {
	return a + a
}
func main(){
	ano(3, tambah)

}