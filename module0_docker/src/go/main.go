package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	fmt.Println("🚀 Go CLI Tool Starting...")
	
	// Demonstrate reading environment variables
	appEnv := os.Getenv("APP_ENV")
	if appEnv == "" {
		appEnv = "development"
	}
	fmt.Printf("Current Environment: %s\n", appEnv)

	// Simulate work
	for i := 1; i <= 5; i++ {
		fmt.Printf("[%s] Processing task %d/5...\n", time.Now().Format("15:04:05"), i)
		time.Sleep(1 * time.Second)
	}

	fmt.Println("✅ Task completed successfully.")
}
