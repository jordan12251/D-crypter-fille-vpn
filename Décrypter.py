import subprocess
import requests
import time
import json

# 🔑 Ton token et chat_id Telegram
TELEGRAM_TOKEN = "7497672818:AAGvj4BL1RE8pkuHi67cBWjUWBVaLfiyGSs"
CHAT_ID = "7874160840"

def get_last_sms():
    try:
        output = subprocess.check_output(["termux>
        sms_list = json.loads(output.decode("utf->
        if sms_list:
            return sms_list[0]  # dernier SMS
    except Exception as e:
        print("Erreur:", e)
    return None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM>
    payload = {"chat_id": CHAT_ID, "text": messag>
    requests.post(url, data=payload)

last_id = None
while True:
    sms = get_last_sms()
    if sms and sms["received"] != last_id:
        sender = sms.get("address", "Inconnu")
        body = sms.get("body", "")
        msg_id = sms.get("received", "")
        formatted = f"📩 Nouveau SMS\n\n👤 De: {s>
        send_telegram(formatted)
        last_id = msg_id
    time.sleep(5)
