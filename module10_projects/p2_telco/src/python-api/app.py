import os
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/usage', methods=['GET'])
def get_usage():
    print("📡 Connecting to MongoDB for real-time usage data...")
    # Simulate DB Check
    mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    time.sleep(1)
    
    return jsonify({
        "status": "online",
        "last_billing_period": "2026-04",
        "data_usage_gb": 45.2,
        "voice_minutes": 120,
        "sms_count": 850
    })

if __name__ == '__main__':
    print("📱 Telco Usage API Starting...")
    app.run(host='0.0.0.0', port=5000)
