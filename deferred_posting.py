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


def create_arguments_parser(default_delay):
    """Parse command-line arguments and return user-entered delay."""
    parser = argparse.ArgumentParser(description='Deferred posting photos to telegram')
    parser.add_argument('delay', help='Enter time between posts', type=int, nargs='?', default=default_delay)
    return parser


def send_delay_message(tg_token, chat_id, delay):
    all_files = list_image_files()
    while True:
        for image in all_files:
            post_image(tg_token, chat_id, file_name=image)
            time.sleep(delay)
        shuffle(all_files)


def main():
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    chat_id = int(os.environ['CHAT_ID'])
    default_delay = int(os.environ['POSTING_DELAY'])
    parser = create_arguments_parser(default_delay)
    arguments = parser.parse_args()
    delay = arguments.delay
    send_delay_message(tg_token, chat_id, delay)


if __name__ == '__main__':
    main()
