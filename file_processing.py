"""Set of functions for working with files.

Functions:
    create_filename(link)
    download_images(images_links, params=None)
    list_image_files()
    get_random_image()
    """
import os
import requests
from random import shuffle
from pathlib import Path
from urllib.parse import urlparse


def create_filename(link):
    filename = os.path.split(urlparse(link).path)[1]
    return filename


def download_images(images_links, params=None):
    Path('./image').mkdir(exist_ok=True)
    if images_links:
        for link in images_links:
            response = requests.get(link, params)
            response.raise_for_status()
            save_path = 'image/{}'.format(create_filename(link))
            with open(save_path, 'wb') as file:
                file.write(response.content)


def list_image_files():
    all_files = []
    for file in os.listdir('image'):
        file_size = os.path.getsize('image/{}'.format(file))
        if file_size <= 20971520:
            all_files.append(file)
        else:
            continue
    return all_files


def get_random_image():
    all_files = list_image_files()
    shuffle(all_files)
    return all_files[0]
