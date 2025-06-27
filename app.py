from flask import Flask, request
import requests
from config import TELEGRAM_TOKEN, CHAT_ID
from datetime import datetime

app = Flask(__name__)

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    symbol = data.get("symbol", "Unknown").upper()
    signal = data.get("signal", "Unknown").upper()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"📢 Trade Signal\n\n🔸 Coin: {symbol}\n🔸 Action: {signal}\n🕒 Time: {now}"
    send_telegram(message)
    return "OK", 200

@app.route("/", methods=["GET"])
def home():
    return "✅ Bot is running!"
