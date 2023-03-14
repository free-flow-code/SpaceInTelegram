from dotenv import load_dotenv
import datetime
from file_processing import *


def get_epic_images():
    """Downloads  Earth Polychromatic Imaging Camera (EPIC) photos"""
    nasa_api_key = os.environ['NASA_API_KEY']
    all_images_link = 'https://api.nasa.gov/EPIC/api/natural/images'
    one_image_link = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}'
    params = {'api_key': nasa_api_key}
    images_links = []
    all_images_response = requests.get(all_images_link, params=params)
    all_images_response.raise_for_status()
    for image in all_images_response.json():
        date = datetime.datetime.strptime(image['date'][:10], '%Y-%m-%d').date()
        path = str(date).replace('-', '/')
        filename = image['image']+'.png'
        download_link = one_image_link.format(path, filename)
        images_links.append(download_link)
    download_images(images_links, params)


if __name__ == '__main__':
    load_dotenv()
    get_epic_images()
