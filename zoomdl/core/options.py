import argparse

class Options:
    _PACKAGE_NAME = 'zoomdl'

    def __init__(self):
        self._parser = argparse.ArgumentParser(prog=self._PACKAGE_NAME,
                                               usage='%(prog)s urls [options]',
                                               description='Download zoom recordings')

        self._create_parser()

    def _create_parser(self) -> None:
        self._parser.add_argument('urls', nargs='+')

        self._parser.add_argument('--no-speaker', '-k', action='store_true',
                                  help="Don't download the speaker screen.")
        self._parser.add_argument('--no-screen', '-c', action='store_true',
                                  help="Don't download the screen share.")
        self._parser.add_argument('--subtitles', '-s', action='store_true',
                                  help="Downloads the default subtitle for the meeting as srt.")
        self._parser.add_argument('--transcription', '-t', action='store_true',
                                  help="Downloads the meeting transcription as srt.")
        self._parser.add_argument('--verbose', '-v', action='store_true',
                                  help="Be more verbose about what is happening.")


    def parse(self, args: list[str]) -> argparse.Namespace:
        return self._parser.parse_args(args)
