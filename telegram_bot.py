"""Posts the specified photo to the channel.
If “what” is not specified, publishes a random photo."""
import os
import random
from dotenv import load_dotenv
import telegram
import argparse
from file_processing import list_image_files


def create_arguments_parser():
    """Parse command-line arguments and return user-entered image file name."""
    parser = argparse.ArgumentParser(description='Publishes images to telegram channel')
    parser.add_argument('file_name', help='Enter file name', nargs='?', default=random.choice(list_image_files()))
    return parser


def post_image(tg_token, chat_id, file_name):
    bot = telegram.Bot(token=tg_token)
    with open('image/{}'.format(file_name), 'rb') as file:
        bot.send_photo(chat_id, photo=file)


def main():
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    chat_id = int(os.environ['CHAT_ID'])
    parser = create_arguments_parser()
    arguments = parser.parse_args()
    file_name = arguments.file_name
    post_image(tg_token, chat_id, file_name)


if __name__ == '__main__':
    main()
