import json

from requests import Session
from requests.models import Response
from requests.exceptions import JSONDecodeError

from zoomdl.handlers.url_handler import UrlHandler
from zoomdl.data.streams import Streams

class DataError(Exception):
    """ Raised when a data error occurs """

class DataHandler:
    _PARAMS = {
        'continueMode': 'true',
    }

    def __init__(self, session: Session, url_handler: UrlHandler) -> None:
        self._session = session
        self._url_handler = url_handler

    def _fetch_content_json(self, url: str, extra_params: dict[str, str]) -> dict[str, str]:
        content_url = self._url_handler.build_content_url(url)

        params = {
            **self._PARAMS,
            **extra_params,
        }

        content_json = self._session.get(
            url=content_url,
            params=params,
        ).json()

        return content_json['result']

    def _content_title(self, content: dict[str, str], curr_clip: int, clips: int) -> str:
        title = content['meet']['topic']
        
        if clips > 1:
            return f'{title} - Recording ({curr_clip}/{clips})'

        return title

    def _fetch_all_clips(self, url: str, params: dict[str, str] = {}) -> list[dict[str, str]]:
        content = self._fetch_content_json(url, params)
        next_clip_start_time = content['nextClipStartTime']

        if next_clip_start_time == -1:
            return [content]

        params = {
            'startTime': next_clip_start_time,
        }

        return [content] + self._fetch_all_clips(url, params)

    def _stream_headers(self, stream_url: str) -> dict[str, str]:
        origin = self._url_handler.origin(stream_url)

        return {
            **self._session.headers,
            'referer': origin,
        }

    def download_stream(self, stream_url: str) -> Response:
        headers = self._stream_headers(stream_url)

        return self._session.get(stream_url, headers=headers, stream=True)

    def fetch_streams(self, url: str) -> Streams:
        try:
            return [Streams(clip) for clip in self._fetch_all_clips(url)]
        except JSONDecodeError as e:
            raise DataError(f'Unable to fetch data as JSON: "{e}"') from e
