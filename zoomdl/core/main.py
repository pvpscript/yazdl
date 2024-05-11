import sys
import requests

from zoomdl.handlers.parser import InfoParser
from zoomdl.handlers.url_handler import UrlHandler
from zoomdl.handlers.data_handler import DataHandler
from zoomdl.core.zoom_downloader import ZoomDownloader

def init_downloader(session: requests.Session) -> ZoomDownloader:
    parser = InfoParser()

    url_handler = UrlHandler(session, parser)
    data_handler = DataHandler(session, url_handler)

    return ZoomDownloader(session, data_handler)

def do_stuff():
    url = sys.argv[1]

    with requests.Session() as session:
        zoom_downloader = init_downloader(session)

        zoom_downloader.download_data(url)

def main():
    print("Entering main")

    do_stuff()
