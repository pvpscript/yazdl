# zoomdl
Download zoom recordings

# Installation
This program can be installed manually, with the source code, using `pip` or, in case you are on Windows, use the latest compiled release.

## Using pip
Simply type the following line into a terminal
```sh
pip install zoomdl
```

## Manually
In case you want to install it directly from the source, simply clone this repository and `cd` into it.

Then, run the following command:
```sh
pip install .
```


# Usage
## Basic usage
```sh
zoomdl recording-url.zoom.us/id1 recording-url.zoom.us/id2 ...
```

This will download all the recordings contained in the given URLs, whose content will be shared screen and speaker cam, if applicable.


## General usage
```sh
zoomdl urls [options]
```

### Options
```sh
  -h, --help           show a help message and exit.
  --no-speaker, -k     Don't download the speaker screen.
  --no-screen, -c      Don't download the screen share.
  --subtitles, -s      Downloads the default subtitle for the meeting as srt.
  --transcription, -t  Downloads the meeting transcription as srt.
```

# Addendum
Just a few things I'd like to add, at least for now.

## DI
When I started writing this script, I decided to use DI in order to make something reusable, which, after a while I realized how much of a overkill this was for such a simple script. At the end, I didn't use [ABCs](https://docs.python.org/3/library/abc.html) and didn't write any tests, so it was a huge waste of time.

I'll eventually fix this mess and add a few tests, but for now, this project is not my top priority.

## YoutubeDL
After I was done with the downloader, I realized that the famous [youtubedl](https://github.com/ytdl-org/youtube-dl) already had a module that downloads zoom recordings, which consists in a very simple and straightforward code, with just a little over 60 lines and also contains proper testing as well, sooo...

But anyway, their script couldn't properly download th recordings that I had, so maybe thua is not that much useless after all?

The thing is, I will improve this script, eventually.

# TODO
Password streams

Use ABC

Write tests lol
