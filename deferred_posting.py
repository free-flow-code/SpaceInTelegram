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
    parser.add_argument('delay', help='Enter time between posts', nargs='?', default=[''])
    return parser


def send_delay_message(delay):
    parser = create_arguments_parser()
    arguments = parser.parse_args()
    if arguments.delay(arguments.integers):
        delay = arguments.delay(arguments.integers)
    all_files = list_image_files()
    while True:
        for image in all_files:
            post_image(file_name=image)
            time.sleep(delay)
        shuffle(all_files)


def main():
    load_dotenv()
    delay = int(os.environ['POSTING_DELAY'])
    send_delay_message(delay)


if __name__ == '__main__':
    main()
