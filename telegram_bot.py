import os
from dotenv import load_dotenv
import telegram


def hello_bot():
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    bot.send_message(text ='Hello world!', chat_id=-1001813053173)


if __name__ == '__main__':
    load_dotenv()
    hello_bot()
