"""Set of functions for working with files."""
import os
import requests
from random import shuffle
from pathlib import Path
from urllib.parse import urlparse


def create_filename(link):
    filename = os.path.split(urlparse(link).path)[1]
    return filename


def download_image(image_link, params=None):
    Path('./image').mkdir(exist_ok=True)
    response = requests.get(image_link, params)
    response.raise_for_status()
    save_path = 'image/{}'.format(create_filename(image_link))
    with open(save_path, 'wb') as file:
        file.write(response.content)


def list_image_files():
    all_files = []
    # The maximum file size for uploading to telegram 20 MB
    max_file_size = 20971520
    for file in os.listdir('image'):
        file_size = os.path.getsize('image/{}'.format(file))
        if file_size <= max_file_size:
            all_files.append(file)
    return all_files


def get_random_image():
    all_files = list_image_files()
    shuffle(all_files)
    return all_files[0]
