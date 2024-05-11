class Streams:
    def __init__(self, content: dict[str, str]) -> None:
        self._content = content

    @property
    def screen(self) -> str:
        return self._content['shareMp4Url']

    @property
    def speaker(self) -> str:
        return self._content['speakerMp4Url']
