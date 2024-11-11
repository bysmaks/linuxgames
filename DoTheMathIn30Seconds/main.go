package main

import (
	"fmt"
	"os"
	"os/exec"
	"strconv"
	"strings"
)

func getPIDs() ([]int, error) {
	cmd := exec.Command("pgrep", "-f", "task.py")
	output, err := cmd.Output()
	if err != nil {
		return nil, err
	}

	pidsStr := strings.Fields(string(output))
	pids := make([]int, len(pidsStr))
	for i, pidStr := range pidsStr {
		pid, err := strconv.Atoi(pidStr)
		if err != nil {
			return nil, err
		}
		pids[i] = pid
	}

	return pids, nil
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ./main <sum_of_pids>")
		os.Exit(1)
	}

	inputSum, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Invalid input. Please provide a valid integer.")
		os.Exit(1)
	}

	pids, err := getPIDs()
	if err != nil {
		fmt.Printf("Error getting PIDs: %v\n", err)
		os.Exit(1)
	}

	sumPIDs := 0
	for _, pid := range pids {
		sumPIDs += pid
	}

	if inputSum == sumPIDs {
		fmt.Println("great flag")
	} else {
		fmt.Println("System will shut down now.")
		cmd := exec.Command("bash", "-c", "shutdown", "-h", "now")
		err := cmd.Run()
		if err != nil {
			fmt.Printf("Error shutting down: %v\n", err)
		}
	}
}
