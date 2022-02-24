import requests
from telegram import Bot

def send_message(BOT_TOKEN, chat_id, message):
    bot = Bot(token=BOT_TOKEN)
    api = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={message.description}'
    response = requests.get(api).json()
    return response['result']
