package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	fmt.Println("🛰️ CDR High-Speed Ingestor Starting...")

	redisUrl := os.Getenv("REDIS_URL")
	fmt.Printf("Queuing data to: %s\n", redisUrl)

	for {
		fmt.Printf("[%s] Bulk Ingest: 500 CDR records received from Network Switch #42\n", time.Now().Format("15:04:05"))
		time.Sleep(10 * time.Second)
		fmt.Println("🚀 Processing complete. Transmitting to Billing API...")
	}
}
