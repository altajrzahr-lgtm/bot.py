import os
import ccxt
from telegram import Bot

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET = os.getenv("BINANCE_SECRET")

exchange = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_SECRET,
    'enableRateLimit': True,
    'options': {'defaultType': 'future'},
    'urls': {
        'api': {
            'public': 'https://testnet.binancefuture.com/fapi/v1',
            'private': 'https://testnet.binancefuture.com/fapi/v1',
        }
    }
})

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send(msg):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)

def main():
    send("🤖 البوت اشتغل بنجاح (Testnet)")
    balance = exchange.fetch_balance()
    usdt = balance['USDT']['total']
    price = exchange.fetch_ticker('BTC/USDT')['last']
    send(f"USDT: {usdt}\nBTC Price: {price}")

if __name__ == "__main__":
    main()
