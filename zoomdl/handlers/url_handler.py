from requests import Session
from urllib.parse import urlparse

from zoomdl.handlers.parser import InfoParser

class UrlHandler:
    _CONTENT_URL_TEMPLATE = '{netloc}/nws/recording/1.0/play/info/{data_portion}'

    def __init__(self, session: Session, parser: InfoParser) -> None:
        self._session = session
        self._parser = parser

    def build_content_url(self, url: str, headers: dict[str, str]) -> None:
        loc = self._build_loc(url)
        data_portion = self._video_data_portion(url, headers)

        return self._build_content_url(loc, data_portion)

    def build_loc(self, url: str) -> str:
        return self._build_loc(url)

    def _build_loc(self, url: str) -> str:
        parsed_url = urlparse(url)

        return f'{parsed_url.scheme}://{parsed_url.netloc}'

    def _video_data_portion(self, url, headers):
        raw_data = self._session.get(url, headers=headers).text
        self._parser.feed(raw_data)

        return self._parser.data

    def _build_content_url(self, loc, data_portion):
        return self._CONTENT_URL_TEMPLATE.format(netloc=loc,
                                                 data_portion=data_portion)
