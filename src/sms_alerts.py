import os
import json
from twilio.rest import Client

# Correct path for `config.json` in the root directory
with open(os.path.join(os.path.dirname(__file__), '..', 'config.json')) as f:
    config = json.load(f)

def send_alert(title, message):
    client = Client(config["twilio_sid"], config["twilio_auth_token"])
    client.messages.create(
        body=f"{title}\n{message}",
        from_=config["twilio_phone_number"],
        to=config["user_phone_number"]
    )