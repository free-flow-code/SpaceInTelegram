"""Publishes all photos from the image directory every 4 hours.

If all photos from the directory are published, the script starts publishing
them again, shuffling the photos in random order.
Posting frequency can be controlled through an environment variable or passed as a command line argument."""
import os
import time
from random import shuffle
from dotenv import load_dotenv
import argparse
from telegram_bot import post_image
from file_processing import list_image_files


def create_arguments_parser():
    """Parse command-line arguments and return user-entered delay."""
    parser = argparse.ArgumentParser(description='Deferred posting photos to telegram')
    parser.add_argument('delay', help='Enter time between posts', type=int, nargs='?', default=None)
    return parser


def send_delay_message(tg_token, chat_id, delay, arguments):
    if arguments.delay:
        delay = arguments.delay
    all_files = list_image_files()
    while True:
        for image in all_files:
            post_image(tg_token, chat_id, arguments=argparse.Namespace(file_name=''), file_name=image)
            time.sleep(delay)
        shuffle(all_files)


def main(arguments):
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    chat_id = int(os.environ['CHAT_ID'])
    delay = int(os.environ['POSTING_DELAY'])
    send_delay_message(tg_token, chat_id, delay, arguments)


if __name__ == '__main__':
    parser = create_arguments_parser()
    arguments = parser.parse_args()
    main(arguments)
