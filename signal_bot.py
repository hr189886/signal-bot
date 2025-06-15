from datetime import datetime
import os
import time
import requests
import telegram

# Telegram setup
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = telegram.Bot(token=TOKEN)

def fetch_price():
    try:
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        data = response.json()
        return float(data["price"])
    except:
        return None

def generate_signal(price):
    if price is None:
        return None
    if price > 60000:
        return "🚀 Buy Signal: BTC is pumping!"
    elif price < 30000:
        return "📉 Sell Signal: BTC is dropping!"
    return None

while True:
    price = fetch_price()
    signal = generate_signal(price)
    if signal:
        bot.send_message(
            chat_id=CHAT_ID,
            text=f"{signal}\n🧠 Price: ${price}\n🕒 {datetime.now().strftime('%Y-%m-%d %I:%M %p')}"
        )
    time.sleep(60)
