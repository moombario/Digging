import os
import json
from flask import Flask, request, render_template
from google.cloud import vision
from src.sms_alerts import send_alert

# Correct path for `config.json` in root directory
with open(os.path.join(os.path.dirname(__file__), '..', 'config.json')) as config_file:
    config = json.load(config_file)

# Set Google Vision API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

# Initialize Vision API Client
client = vision.ImageAnnotatorClient()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test_alert', methods=['POST'])
def test_alert():
    send_alert("Test Alert", "This is a test notification.")
    return "Test alert sent successfully."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))