import re

from typing import Generator

from requests import Session

from zoomdl.handlers.data_handler import DataHandler

DownloadCoroutine = Generator[bytes, None, None]

class ZoomDownloader:
    _CHUNK_SIZE = 1048576 # 1MiB

    def __init__(self, args: list[str], session: Session, data_handler: DataHandler) -> None:
        self._args = args
        self._session = session
        self._data_handler = data_handler

    def _download_stream(self, url: str) -> DownloadCoroutine:
        with self._data_handler.download_stream(url) as video_stream:
            video_stream.raise_for_status() 

            yield from video_stream.iter_content(chunk_size=self._CHUNK_SIZE)

    def _test(self, url, name_tmp):
        with open(name_tmp, 'wb') as f:
            i = 0

            x = self._download_stream(url)
            for chunk in x:
                if i > 100:
                    break

                print(i)
                f.write(chunk)
                i += 1

    def _download_to_file(self, url: str, name: str) -> None:
        with open(name, 'wb') as output:
            for chunk in self._download_stream(url):
                output.write(chunk)

    def download_data(self, url: str) -> None:
        streams = self._data_handler.fetch_streams(url)

        for stream in streams:
            self._download_to_file(stream.speaker, stream.title + ' - Speaker.mp4')
            self._download_to_file(stream.screen, stream.title + ' - Screen.mp4')
