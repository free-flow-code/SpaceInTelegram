from dotenv import load_dotenv
import datetime
from file_processing import *


def get_epic_images(nasa_api_key):
    """Downloads  Earth Polychromatic Imaging Camera (EPIC) photos"""
    all_images_link = 'https://api.nasa.gov/EPIC/api/natural/images'
    one_image_link = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}'
    params = {'api_key': nasa_api_key}
    all_images_response = requests.get(all_images_link, params=params)
    all_images_response.raise_for_status()
    for image in all_images_response.json():
        date = datetime.datetime.strptime(image['date'][:10], '%Y-%m-%d').date()
        path = str(date).replace('-', '/')
        filename = image['image']+'.png'
        image_link = one_image_link.format(path, filename)
        download_image(image_link, params=params)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    get_epic_images(nasa_api_key)


if __name__ == '__main__':
    main()
