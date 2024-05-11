import json

from requests import Session
from requests.exceptions import JSONDecodeError

from zoomdl.handlers.url_handler import UrlHandler
from zoomdl.data.streams import Streams
from zoomdl.data.headers import ua_header

class DataError(Exception):
    """ Raised when a data error occurs """

class DataHandler:
    _PARAMS = {
        'continueMode': 'true',
    }

    def __init__(self, session: Session, url_handler: UrlHandler) -> None:
        self._session = session
        self._url_handler = url_handler

    def _fetch_content_json(self, url: str) -> dict[str, str]:
        content_url = self._url_handler.build_content_url(url, ua_header)

        content_json = self._session.get(
            url=content_url,
            headers=ua_header,
            params=self._PARAMS
        ).json()

        return content_json['result']

    def content_header(self, url):
        loc = self._url_handler.build_loc(url)

        return {
            **ua_header,
            'referer': loc
        }

    def fetch_streams(self, url: str) -> Streams:
        try:
            return Streams(self._fetch_content_json(url))
        except JSONDecodeError as e:
            raise DataError(f'Unable to fetch data as JSON: "{e}"') from e
