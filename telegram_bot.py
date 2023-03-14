import os
from dotenv import load_dotenv
import telegram


def hello_bot():
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    print(bot.getMe())


if __name__ == '__main__':
    load_dotenv()
    hello_bot()
