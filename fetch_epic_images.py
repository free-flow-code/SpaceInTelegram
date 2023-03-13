import datetime
from file_processing import *


def fetch_epic_images(nasa_api_key):
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
