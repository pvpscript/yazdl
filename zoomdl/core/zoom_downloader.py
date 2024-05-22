import re

from typing import Generator

from requests import Session

from zoomdl.handlers.data_handler import DataHandler

DownloadCoroutine = Generator[bytes, None, None]

class ZoomDownloader:
    _CHUNK_SIZE = 1024 * 64 # 64KiB

    def __init__(self, args: list[str], session: Session, data_handler: DataHandler) -> None:
        self._args = args
        self._session = session
        self._data_handler = data_handler

    def _download_stream(self, url: str) -> None:
        video_stream = self._data_handler.download_stream(url)
        video_stream.raise_for_status() 

        stream = video_stream.raw
        size = int(stream.headers['Content-Length'])

        return stream, size

    def _download_to_file(self, url: str, output_file_name: str) -> None:
        stream, size = self._download_stream(url)

        i = 1
        dots_mod = 4

        print(f'Downloading file: "{output_file_name}"')

        with open(output_file_name, 'wb') as output:
            while data := stream.read(self._CHUNK_SIZE):
                output.write(data)

                print(f'Downloading{"."*i}{" "*(dots_mod - i)}', end='\r')
                i = (i + 1) % 4

        print('\nFinished downloading file!')

        stream.close()

    def download_data(self, url: str) -> None:
        streams = self._data_handler.fetch_streams(url)
        
        for stream in streams:
            self._download_to_file(stream.speaker, stream.title + ' - Speaker.mp4')
            self._download_to_file(stream.screen, stream.title + ' - Screen.mp4')
            self._download_to_file(stream.subtitles, stream.title + ' - Subtitles.srt')
            self._download_to_file(stream.transcription, stream.title + ' - Transcription.srt')
