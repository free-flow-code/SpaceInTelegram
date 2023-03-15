"""Set of functions for working with files."""
import os
import requests
from random import shuffle
from pathlib import Path
from urllib.parse import urlparse


def download_image(image_link, params=None):
    Path('./image').mkdir(exist_ok=True)
    response = requests.get(image_link, params)
    response.raise_for_status()
    file_name = os.path.split(urlparse(image_link).path)[1]
    save_path = 'image/{}'.format(file_name)
    with open(save_path, 'wb') as file:
        file.write(response.content)


def list_image_files():
    all_files = []
    max_size_telegram_file = 20971520
    for file in os.listdir('image'):
        file_size = os.path.getsize('image/{}'.format(file))
        if file_size <= max_size_telegram_file:
            all_files.append(file)
    return all_files


def get_random_image():
    all_files = list_image_files()
    shuffle(all_files)
    return all_files[0]
