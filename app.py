from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = '8015389092:AAGw0WA-5iqVAteZgtqnsnepi_KNj2JR_zY'
TELEGRAM_CHAT_ID = '7918579140'

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': text}
    requests.post(url, json=data)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return 'No data received', 400

    signal = data.get('signal')
    symbol = data.get('symbol', 'UNKNOWN')
    price = data.get('price', '???')
    time = data.get('time', '')

    msg = f"📡 Signal: {signal}\n📈 Symbol: {symbol}\n💰 Price: {price}\n🕒 Time: {time}"
    send_telegram_message(msg)

    return {'status': 'received'}, 200
