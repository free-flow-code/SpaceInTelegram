import os
from urllib.parse import urlparse


def create_filename(link):
    filename = os.path.split(urlparse(link).path)[1]
    return filename
