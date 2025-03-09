from twilio.rest import Client
import json

# Load config
with open('config.json') as f:
    config = json.load(f)

def send_alert(title, message):
    client = Client(config["twilio_sid"], config["twilio_auth_token"])
    client.messages.create(
        body=f"{title}\n{message}",
        from_=config["twilio_phone_number"],
        to=config["user_phone_number"]
    )