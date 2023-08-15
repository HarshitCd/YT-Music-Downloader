from ytmusicapi import YTMusic

def add_likes_to_playlist() -> list:

    ytmusic = YTMusic('oauth.json')
    liked = ytmusic.get_liked_songs(1000)
    likedIDs = []

    for song in liked['tracks']:
        likedIDs.append(song["videoId"])

    ytmusic.create_playlist("Liked Songs", "Liked Song playlist duplicate", "PUBLIC", likedIDs, "")