package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ./main <pin_code>")
		os.Exit(1)
	}

	pinCode := os.Args[1]

	if pinCode == "15627" {
		fmt.Println("you flag is super_pin_code_brure")
	} else {
		fmt.Println("Invalid pin code")
	}
}
