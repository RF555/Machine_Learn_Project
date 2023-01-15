"""
code below was found in https://opendatascience.com/a-machine-learning-deep-dive-into-my-spotify-data/
and well be using spotipy doc dound in https://spotipy.readthedocs.io/en/2.22.0/
"""

import pandas as pd
import spotipy


def getPlaylistData(plalist_id="78JTO1LbTGeD4kF8ACBQsC"):
    from spotipy.oauth2 import SpotifyClientCredentials
    spotify = spotipy.Spotify()
    cid = "bfac9b315dac4c499fd2fe150e6d5697"  # CLIENT ID
    secret = "fc3d2ba5d1264f0db507c8ac49ebcc7c"  # CLIENT SECRET
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    spotify.trace = False
    playlist = spotify.playlist(plalist_id)
    # playlist = spotify.user_playlist("roey.feingold", "Roey")
    songs = playlist["tracks"]["items"]
    ids = []
    for i in range(len(songs)):
        ids.append(songs[i]["track"]["id"])
    features = spotify.audio_features(ids)
    df = pd.DataFrame(features)
    print(df)
