import requests
from pathlib import Path
import create_filename


def fetch_apod_images(nasa_api_key):
    """Downloads Astronomy Picture of the Day (APOD)"""
    Path('./image').mkdir(exist_ok=True)
    apod_link = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_api_key,
              'count': 30}
    apod_response = requests.get(apod_link, params=params)
    apod_response.raise_for_status()
    for images in apod_response.json():
        image_response = requests.get(images['url'], params=params)
        image_response.raise_for_status()
        save_path = 'image/{}'.format(create_filename(link=images['url']))
        with open(save_path, 'wb') as file:
            file.write(image_response.content)
