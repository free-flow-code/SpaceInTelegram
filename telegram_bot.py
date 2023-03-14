import os
from dotenv import load_dotenv
import telegram


def hello_bot():
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    #bot.send_message(text ='Hello world!', chat_id=-1001813053173)
    #bot.send_chat_action(chat_id=-1001813053173, action=message.UPLOAD_PHOTO)
    bot.send_photo(-1001813053173,
                   'https://github.com/free-flow-code/SpaceInTelegram/blob/main/image/AndromedaGalex_900.jpg?raw=true'
                   )


if __name__ == '__main__':
    load_dotenv()
    hello_bot()
