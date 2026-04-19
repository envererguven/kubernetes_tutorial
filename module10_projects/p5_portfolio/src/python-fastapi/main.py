import time

print("📈 Portfolio Risk Calculator (FastAPI Engine) Starting...")

def compute_var():
    print("🧮 Running Monte Carlo simulation for Portfolio X...")
    time.sleep(2)
    return 0.125  # 12.5% VaR

while True:
    var = compute_var()
    print(f"[{time.strftime('%H:%M:%S')}] Current Value at Risk (VaR): {var*100}%")
    print("📥 Syncing results to TimescaleDB...")
    time.sleep(10)
