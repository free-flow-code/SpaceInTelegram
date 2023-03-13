import os
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_images
from fetch_apod_images import fetch_apod_images
from fetch_epic_images import fetch_epic_images


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_spacex_images()
    #fetch_apod_images(nasa_api_key)
    #fetch_epic_images(nasa_api_key)


if __name__ == '__main__':
    main()
