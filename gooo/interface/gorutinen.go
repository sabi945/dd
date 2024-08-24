package main
import (
	"fmt"
	"time"
)
func printNumbers() {
    for i := 1; i <= 5; i++ {
        fmt.Println(i)
        time.Sleep(1 * time.Second) // Menunggu 1 detik
    }
}

func main() {
    // Membuat goroutine dengan menggunakan kata kunci go
    go printNumbers()

    // Menunggu agar program tidak berakhir terlalu cepat
    // Sehingga goroutine memiliki kesempatan untuk dijalankan
    time.Sleep(3 * time.Second)

    fmt.Println("Selesai menjalankan goroutine")
}