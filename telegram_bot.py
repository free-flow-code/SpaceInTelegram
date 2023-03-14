import os
from dotenv import load_dotenv
import telegram
import argparse


def create_arguments_parser():
    """Parse command-line arguments and return user-entered launch ID."""
    parser = argparse.ArgumentParser(description='Publishes images to telegram channel')
    parser.add_argument('launch_id', help='Enter file name', nargs='?', default=[''])
    return parser


def post_image():
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    parser = create_arguments_parser()
    arguments = parser.parse_args()
    file_name = arguments.launch_id[0:]
    if file_name:
        bot.send_photo(-1001813053173, photo=open('image/{}'.format(file_name), 'rb'))
    else:
        bot.send_photo(-1001813053173, photo=open('image/{}'.format(get_random_image()), 'rb'))


if __name__ == '__main__':
    load_dotenv()
    post_image()
