import yt_dlp as youtube_dl
import os

def audio_downloader(url: str) -> None:
    download_location = os.environ['DOWNLOAD_PATH']
    opts = {
        'format': 'bestaudio/best',  # Choose best audio format
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',   # Convert to MP3 format
            'preferredquality': '192', # MP3 quality
        }],
        'outtmpl': download_location + '%(title)s.%(ext)s',  # Output file name template
    }
    audio_downloader = youtube_dl.YoutubeDL(opts)
    audio_downloader.extract_info(url)