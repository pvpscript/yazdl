from requests import Session

from typing import Generator

from zoomdl.handlers.data_handler import DataHandler

DownloadCoroutine = Generator[bytes, None, None]

class ZoomDownloader:
    def __init__(self, session: Session, data_handler: DataHandler) -> None:
        self._session = session
        self._data_handler = data_handler

    def _download_stream(self, url: str, headers: dict[str, str]) -> DownloadCoroutine:
        with self._session.get(url, headers=headers, stream=True) as video:
            video.raise_for_status()

            yield from video.iter_content(chunk_size=8192)

    def _test(self, url, headers, name_tmp):
        with open(name_tmp, 'wb') as f:
            i = 0

            x = self._download_stream(url, headers)
            for chunk in x:
                if i > 1024:
                    break

                print(i)
                f.write(chunk)
                i += 1


    def download_data(self, url: str) -> None:
        headers = self._data_handler.content_header(url)
        streams = self._data_handler.fetch_streams(url)

        self._test(streams.speaker, headers, 'speaker.mp4')
        self._test(streams.screen, headers, 'screen.mp4')
