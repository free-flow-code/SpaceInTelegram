"""Posts the specified photo to the channel.
If “what” is not specified, publishes a random photo."""
import os
from dotenv import load_dotenv
import telegram
import argparse
from file_processing import get_random_image


def create_arguments_parser():
    """Parse command-line arguments and return user-entered image file name."""
    parser = argparse.ArgumentParser(description='Publishes images to telegram channel')
    parser.add_argument('file_name', help='Enter file name', nargs='?', default=[''])
    return parser


def post_image(file_name=None):
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    if not file_name:
        parser = create_arguments_parser()
        arguments = parser.parse_args()
        file_name = arguments.file_name[0:0]
        if file_name:
            bot.send_photo(-1001813053173, photo=open('image/{}'.format(file_name), 'rb'))
        else:
            bot.send_photo(-1001813053173, photo=open('image/{}'.format(get_random_image()), 'rb'))
    else:
        bot.send_photo(-1001813053173, photo=open('image/{}'.format(file_name), 'rb'))


if __name__ == '__main__':
    post_image()
