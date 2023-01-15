"""
code below was found in https://opendatascience.com/a-machine-learning-deep-dive-into-my-spotify-data/
and well be using spotipy doc dound in https://spotipy.readthedocs.io/en/2.22.0/
"""

import pandas as pd
import spotipy

CLIENT = pd.read_csv("Spotify Clients.csv")
CLIENT_ID = CLIENT.iloc[0][0]  # CLIENT ID
CLIENT_SECRET = CLIENT.iloc[0][1]  # CLIENT SECRET


def getPlaylistData(plalist_id):
    from spotipy.oauth2 import SpotifyClientCredentials
    spotify = spotipy.Spotify()
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
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
