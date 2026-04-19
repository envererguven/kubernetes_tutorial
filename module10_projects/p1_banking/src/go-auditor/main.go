package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	fmt.Println("🔍 Ledger Auditor Starting...")

	dbUrl := os.Getenv("DB_URL")
	fmt.Printf("Monitoring Ledger at: %s\n", dbUrl)

	// Simulate periodic auditing
	for {
		fmt.Printf("[%s] Audit Check: Verifying checksums for last 100 transactions...\n", time.Now().Format("15:04:05"))
		time.Sleep(15 * time.Second)
		fmt.Println("✅ Audit Passed. No discrepancies found.")
		time.Sleep(5 * time.Second)
	}
}
