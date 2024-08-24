package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup

	// Menjalankan goroutine untuk fungsi tanpa perulangan
	wg.Add(1)
	go fungsiTanpaPerulangan(&wg)

	// Menunggu selesai goroutine
	wg.Wait()

	fmt.Println("Selesai")
}

func fungsiTanpaPerulangan(wg *sync.WaitGroup) {
	defer wg.Done()

	fmt.Println("Mulai eksekusi fungsi tanpa perulangan")

	// Melakukan beberapa tugas di sini
	time.Sleep(2 * time.Second)

	fmt.Println("Selesai eksekusi fungsi tanpa perulangan")
}
