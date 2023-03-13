"""Loads a photo from SpaceX at the specified launch ID.
If the launch ID is not specified, downloads the photo from the last launch.

Functions:
    get_spacex_images_links()
    fetch_spacex_images()
"""
import requests
from pathlib import Path
import create_filename


def get_spacex_images_links():
    latest_launch = 'https://api.spacexdata.com/v5/launches/latest'
    past_launches = 'https://api.spacexdata.com/v5/launches/past'
    id_launch = 'https://api.spacexdata.com/v5/launches/{}'
    ll_response = requests.get(latest_launch)
    ll_response.raise_for_status()
    if not ll_response.json()['links']['flickr']['original']:
        pl_response = requests.get(past_launches)
        pl_response.raise_for_status()
        for launch in pl_response.json():
            id_response = requests.get(id_launch.format(launch['id']))
            id_response.raise_for_status()
            if id_response.json()['links']['flickr']['original']:
                return id_response.json()['links']['flickr']['original']
                break
    else:
        return ll_response.json()['links']['flickr']['original']


def fetch_spacex_images():
    """Downloads photos from the last SpaceX launch"""
    Path('./image').mkdir(exist_ok=True)
    images_links = get_spacex_images_links()
    for link in images_links:
        response = requests.get(link)
        response.raise_for_status()
        save_path = 'image/{}'.format(create_filename(link))
        with open(save_path, 'wb') as file:
            file.write(response.content)
