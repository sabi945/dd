package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	// WaitGroup digunakan untuk menunggu selesainya semua goroutine
	var wg sync.WaitGroup

	// Jumlah goroutine yang akan dijalankan
	jumlahGoroutine := 3

	// Menambahkan jumlah goroutine ke WaitGroup
	wg.Add(jumlahGoroutine)

	// Goroutine pertama
	go func() {
		defer wg.Done() // Memberi tahu WaitGroup bahwa goroutine telah selesai
		for i := 1; i <= 5; i++ {
			fmt.Println("Goroutine 1 - Iterasi", i)
			time.Sleep(time.Millisecond * 500)
		}
	}()

	// Goroutine kedua
	go func() {
		defer wg.Done()
		for i := 1; i <= 3; i++ {
			fmt.Println("Goroutine 2 - Iterasi", i)
			time.Sleep(time.Millisecond * 700)
		}
	}()

	// Goroutine ketiga
	go func() {
		defer wg.Done()
		for i := 1; i <= 4; i++ {
			fmt.Println("Goroutine 3 - Iterasi", i)
			time.Sleep(time.Millisecond * 600)
		}
	}()

	// Menunggu semua goroutine selesai
	wg.Wait()

	fmt.Println("Semua goroutine selesai. Program berakhir.")
}
