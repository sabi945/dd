package main

import "fmt"

func factorial(n int) int {
    // Base case: jika n adalah 0 atau 1, kembalikan 1
    if n == 0 || n == 1 {
        return 1
    }
    // Rekursif: Hitung faktorial dari n-1 dan kalikan dengan n
    return n * factorial(n-1)
}

func main() {
    // Panggil fungsi factorial dengan argumen 5
    result := factorial(5)
    fmt.Println("Faktorial dari 5 adalah:", result)
}
