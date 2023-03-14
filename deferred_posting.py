"""Publishes all photos from the image directory every 4 hours.
If all photos from the directory are published, the script starts publishing
them again, shuffling the photos in random order."""
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
    parser.add_argument('delay', help='Enter time between posts', nargs='?', default=['14400'])
    return parser


def tg_auto_posting():
    load_dotenv()
    delay = 14400
    first_start = True
    try:
        delay = int(os.environ['POSTING_DELAY'])
    except KeyError:
        parser = create_arguments_parser()
        arguments = parser.parse_args()
        delay = int(arguments.delay[0])
    while True:
        if first_start:
            all_files = list_image_files()
            for image in all_files:
                post_image(image)
                time.sleep(delay)
            first_start = False
        else:
            shuffle(all_files)
            for image in all_files:
                post_image(image)
                time.sleep(delay)


if __name__ == '__main__':
    tg_auto_posting()
