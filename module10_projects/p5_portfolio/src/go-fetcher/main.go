package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("📊 Real-Time Market Data Fetcher Starting...")

	for {
		fmt.Printf("[%s] Fetching AAPL, MSFT, GOOGL prices from external provider...\n", time.Now().Format("15:04:05"))
		time.Sleep(1 * time.Second)
		fmt.Println("🛰️ Data received. Updating shared Redis memory...")
		time.Sleep(4 * time.Second)
	}
}
