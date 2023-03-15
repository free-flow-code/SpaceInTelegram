import os
import requests
from dotenv import load_dotenv
from file_processing import download_image


def get_apod_images(nasa_api_key):
    """Downloads Astronomy Picture of the Day (APOD)"""
    apod_link = 'https://api.nasa.gov/planetary/apod'
    number_images_download = 30
    params = {'api_key': nasa_api_key,
              'count': number_images_download}
    apod_response = requests.get(apod_link, params=params)
    apod_response.raise_for_status()
    images = apod_response.json()
    for image in images:
        download_image(image_link=image['url'], params=params)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    get_apod_images(nasa_api_key)


if __name__ == '__main__':
    main()
