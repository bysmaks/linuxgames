package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, World! This is a flag: port_knocking_service.")
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Starting server on port 4444...")
    if err := http.ListenAndServe(":4444", nil); err != nil {
        fmt.Printf("Error starting server: %s\n", err)
    }
}
