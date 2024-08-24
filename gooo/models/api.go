package main

import (
    "fmt"
    "net/http"
)

var tulisan string

func main() {
    tulisan = "API dijala"

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, tulisan)
    })

    http.ListenAndServe(":8081", nil)
}
