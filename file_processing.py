import os
import requests
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
