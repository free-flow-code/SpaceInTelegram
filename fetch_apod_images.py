from dotenv import load_dotenv
from file_processing import *


def get_apod_images():
    """Downloads Astronomy Picture of the Day (APOD)"""
    nasa_api_key = os.environ['NASA_API_KEY']
    apod_link = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_api_key,
              'count': 3}
    apod_response = requests.get(apod_link, params=params)
    apod_response.raise_for_status()
    images = apod_response.json()
    images_links = []
    for image in images:
        images_links.append(image['url'])
    download_images(images_links, params)


if __name__ == '__main__':
    load_dotenv()
    get_apod_images()
