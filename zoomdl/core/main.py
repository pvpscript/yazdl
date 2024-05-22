import sys
import requests

from zoomdl.handlers.parser import InfoParser
from zoomdl.handlers.url_handler import UrlHandler
from zoomdl.handlers.data_handler import DataHandler
from zoomdl.core.zoom_downloader import ZoomDownloader
from zoomdl.core.headers import default_headers


def init_downloader(args: list[str], session: requests.Session) -> ZoomDownloader:
    parser = InfoParser()

    url_handler = UrlHandler(session, parser)
    data_handler = DataHandler(session, url_handler)

    return ZoomDownloader(args, session, data_handler)

def start_session(args: list[str]) -> None:
    url = args[1]

    with requests.Session() as session:
        session.headers = default_headers

        zoom_downloader = init_downloader(args, session)

        zoom_downloader.download_data(url)

def main() -> None:
    start_session(sys.argv)
