import re

class Streams:
    def __init__(self, content: dict[str, str]) -> None:
        self._content = content

    @property
    def screen(self) -> str:
        return self._content['shareMp4Url']

    @property
    def speaker(self) -> str:
        return self._content['speakerMp4Url']

    def _sanitize(self, string: str) -> str:
        return re.sub(r'[^ a-zA-Z0-9_{}()-]', '_', string)

    @property
    def title(self) -> str:
        title = self._content['meet']['topic']
        clips = self._content['totalClips']
        curr_clip = self._content['currentClip']
        
        if clips > 1:
            return self._sanitize(f'{title} - Recording {curr_clip} of {clips}')

        return self._sanitize(title)
