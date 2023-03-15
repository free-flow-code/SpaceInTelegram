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
    parser.add_argument('launch_id', help='Enter launch ID', nargs='?', default='latest')
    return parser


def get_spacex_images_links(launch_id):
    site = 'https://api.spacexdata.com/v5/launches/{}'.format(launch_id)
    ll_response = requests.get(site)
    ll_response.raise_for_status()
    return ll_response.json()['links']['flickr']['original']


def get_spacex_images():
    parser = create_arguments_parser()
    arguments = parser.parse_args()
    launch_id = arguments.launch_id
    for image_link in get_spacex_images_links(launch_id):
        download_image(image_link)


if __name__ == '__main__':
    get_spacex_images()
