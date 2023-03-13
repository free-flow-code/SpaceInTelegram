import requests
import datetime
import os
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv


def create_filename(link):
    filename = os.path.split(urlparse(link).path)[1]
    return filename


def get_links():
    """Gets photos from the last SpaceX launch"""
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


def fetch_spacex_last_launch():
    """Downloads photos from the last SpaceX launch"""
    Path('./image').mkdir(exist_ok=True)
    images_links = get_links()
    for link in images_links:
        response = requests.get(link)
        response.raise_for_status()
        save_path = 'image/{}'.format(create_filename(link))
        with open(save_path, 'wb') as file:
            file.write(response.content)


def get_apod_photos(nasa_api_key):
    """Downloads Astronomy Picture of the Day (APOD)"""
    Path('./image').mkdir(exist_ok=True)
    apod_link = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_api_key,
              'count': 3}
    apod_response = requests.get(apod_link, params=params)
    apod_response.raise_for_status()
    for images in apod_response.json():
        image_response = requests.get(images['url'], params=params)
        image_response.raise_for_status()
        save_path = 'image/{}'.format(create_filename(link=images['url']))
        with open(save_path, 'wb') as file:
            file.write(image_response.content)


def get_epic_photos(nasa_api_key):
    """Downloads  Earth Polychromatic Imaging Camera (EPIC) photos"""
    Path('./image').mkdir(exist_ok=True)
    all_images_link = 'https://api.nasa.gov/EPIC/api/natural/images'
    one_image_link = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}'
    params = {'api_key': nasa_api_key}
    all_images_response = requests.get(all_images_link, params=params)
    all_images_response.raise_for_status()
    for image in all_images_response.json():
        date = datetime.datetime.strptime(image['date'][:10], '%Y-%m-%d').date()
        path = str(date).replace('-', '/')
        filename = image['image']+'.png'
        download_link = one_image_link.format(path, filename)
        one_image_response = requests.get(download_link, params=params)
        one_image_response.raise_for_status()
        save_path = 'image/{}'.format(create_filename(link=download_link))
        with open(save_path, 'wb') as file:
            file.write(one_image_response.content)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    #fetch_spacex_last_launch()
    get_apod_photos(nasa_api_key)
    #get_epic_photos(nasa_api_key)


if __name__ == '__main__':
    main()
