"""Loads a photo from SpaceX at the specified launch ID.
If the launch ID is not specified, downloads the photo from the last launch.

Functions:
    create_arguments_parser()
    get_id_images_links(launch_id)
    get_ll_images_links()
    get_spacex_images()
"""
import argparse
from file_processing import *


def create_arguments_parser():
    """Parse command-line arguments and return user-entered launch ID."""
    parser = argparse.ArgumentParser(description='Download images of SpaceX launches')
    parser.add_argument('launch_id', help='Enter launch ID', nargs='?', default='')
    return parser


def get_id_images_links(launch_id):
    site = 'https://api.spacexdata.com/v5/launches/{}'
    id_response = requests.get(site.format(launch_id))
    id_response.raise_for_status()
    return id_response.json()['links']['flickr']['original']


def get_ll_images_links():
    latest_launch = 'https://api.spacexdata.com/v5/launches/latest'
    ll_response = requests.get(latest_launch)
    ll_response.raise_for_status()
    return ll_response.json()['links']['flickr']['original']


def get_spacex_images():
    parser = create_arguments_parser()
    arguments = parser.parse_args()
    launch_id = arguments.launch_id
    if launch_id:
        for image_link in get_id_images_links(launch_id):
            download_image(image_link)
    else:
        # ll - latest launch
        for image_link in get_ll_images_links():
            download_image(image_link)


if __name__ == '__main__':
    get_spacex_images()
