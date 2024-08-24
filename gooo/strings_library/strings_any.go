package main

import (
	"fmt"
	"strings"
)

func main() {
	said := "hallo"

	fmt.Println(strings.ContainsAny(said,"o"))


	s := "Hello, world!"
    
    isVowel := func(r rune) bool {
        return strings.ContainsRune("aeiouAEIOU", r)
    }
	fmt.Println(strings.ContainsFunc(s,isVowel))

}