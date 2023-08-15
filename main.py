from ytmusicapi import YTMusic
import ytaudio.ytaudio as yta
import concurrent.futures
import subprocess


def get_music_links() -> list:
    ytmusic = YTMusic('oauth.json')
    liked = ytmusic.get_liked_songs(1000)
    links = []

    for song in liked['tracks']:
        links.append(f"https://music.youtube.com/watch?v={song['videoId']}")

    return links

def convert_mp4_to_mp3(filename: str) -> None:
    try:
        print(filename)
        subprocess.run(filename, shell=True)
    except Exception as e:
        print(e)

def main():
    links = get_music_links()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(yta.audio_downloader, links)
    

if __name__ == '__main__':
    main()