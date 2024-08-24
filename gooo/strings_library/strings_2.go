package main

import (
    "fmt"
    "strings"
)

func main() {
    str1 := "fpple"
    str2 := "banana"

    result := strings.Compare(str1, str2)

    if result < 0 {
        fmt.Printf("%s comes before %s\n", str1, str2)
    } else if result > 0 {
        fmt.Printf("%s comes after %s\n", str1, str2)
    } else {
        fmt.Printf("%s and %s are equal\n", str1, str2)
    }
}
