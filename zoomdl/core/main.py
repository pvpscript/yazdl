import sys
import requests

from argparse import Namespace

from zoomdl.handlers.parser import InfoParser
from zoomdl.handlers.url_handler import UrlHandler
from zoomdl.handlers.data_handler import DataHandler
from zoomdl.core.zoom_downloader import ZoomDownloader
from zoomdl.core.headers import default_headers
from zoomdl.core.options import Options


def init_downloader(args: Namespace, session: requests.Session) -> ZoomDownloader:
    parser = InfoParser()
    url_handler = UrlHandler(session, parser)
    data_handler = DataHandler(session, url_handler)

    return ZoomDownloader(args, data_handler)

def start_session(args: Namespace) -> None:
    with requests.Session() as session:
        session.headers = default_headers

        zoom_downloader = init_downloader(args, session)

        for url in args.urls:
            zoom_downloader.download_data(url)

def main() -> None:
    options = Options()
    parsed_args = options.parse(sys.argv[1:])

    start_session(parsed_args)
