package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"time"
)

const filePath = "/data/counter.txt"

func main() {
	fmt.Println("💾 Persistent Go App Starting...")

	for {
		count := readCounter()
		count++
		writeCounter(count)
		fmt.Printf("[%s] Counter incremented to: %d\n", time.Now().Format("15:04:05"), count)
		time.Sleep(10 * time.Second)
	}
}

func readCounter() int {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		if os.IsNotExist(err) {
			return 0
		}
		fmt.Printf("Error reading file: %v\n", err)
		return 0
	}
	val, err := strconv.Atoi(strings.TrimSpace(string(data)))
	if err != nil {
		return 0
	}
	return val
}

func writeCounter(val int) {
	err := ioutil.WriteFile(filePath, []byte(strconv.Itoa(val)), 0644)
	if err != nil {
		fmt.Printf("Error writing file: %v\n", err)
	}
}
