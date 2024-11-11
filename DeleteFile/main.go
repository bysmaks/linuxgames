package main

import (
	"fmt"
	"os"
)

func main() {
	filePath := "/root/dontdelete"
	if _, err := os.Stat(filePath); err == nil {
		fmt.Println("File exists")
	} else if os.IsNotExist(err) {
		fmt.Println("flag: f3334634006f810113f4d18526d3ea11")
	} else {
		fmt.Println("Error checking file:", err)
	}
}
