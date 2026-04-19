package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("⚡ High-Frequency Order Matcher Starting...")

	for {
		fmt.Println("--- NEW TICK ---")
		fmt.Printf("[%s] Matching BUY 1.5 BTC @ $60k with SELL 1.5 BTC @ $60k\n", time.Now().Format("15:04:05"))
		time.Sleep(2 * time.Second)
		fmt.Println("✅ Trade Executed. Updating order book in Redis...")
		time.Sleep(8 * time.Second)
	}
}
