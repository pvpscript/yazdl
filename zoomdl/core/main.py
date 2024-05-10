import sys
import requests

from urllib.parse import urlparse
from typing import Self

from zoomdl.handlers.parser import InfoParser
from zoomdl.handlers.url_handler import UrlHandler
from zoomdl.handlers.data_handler import DataHandler
from zoomdl.core.zoom_downloader import ZoomDownloader

def init_downloader(session: requests.Session) -> ZoomDownloader:
    from zoomdl.handlers import (parser, url_handler, data_handler)
    parser = parser.InfoParser()

    url_handler = url_handler.UrlHandler(session, parser)
    data_handler = data_handler.DataHandler(session, url_handler)

    return ZoomDownloader(session, data_handler)

def do_stuff():
    url = sys.argv[1]

    with requests.Session() as session:
        zoom_downloader = init_downloader(session)

        zoom_downloader.download_data(url)

def main():
    print("Entering main")

    do_stuff()
