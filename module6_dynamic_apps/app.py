import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # These will be provided by Kubernetes ConfigMaps and Secrets
    greeting = os.getenv('APP_GREETING', 'Default Greeting')
    db_pass = os.getenv('DB_PASSWORD', 'No Password Found')
    return f"""
    <html>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
            <h1>{greeting}</h1>
            <p style="color: #666;">Secret retrieved from K8s: <b>{db_pass}</b></p>
            <hr width="50%">
            <p>Pod Name: {os.getenv('HOSTNAME', 'Unknown')}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
