package main

import (
    "net/http"
    "html/template"
)

func main() {
    http.HandleFunc("/", handler)
    http.HandleFunc("/submit", submitHandler)
    http.ListenAndServe(":8090", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
    tmpl, err := template.ParseFiles("contoh-form.html")
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    tmpl.Execute(w, nil)
}

func submitHandler(w http.ResponseWriter, r *http.Request) {
    // Handle aksi dari form di sini
    // ...
    http.Redirect(w, r, "/", http.StatusSeeOther)
}