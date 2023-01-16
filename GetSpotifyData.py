"""
We used the code found in https://opendatascience.com/a-machine-learning-deep-dive-into-my-spotify-data/

We'll be using spotipy doc dound in https://spotipy.readthedocs.io/en/2.22.0/
"""

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ = pd.read_csv("Spotify Clients.csv")
ROEY_FEINGOLD_CLIENT = CLIENT_.iloc[0]
ROEY_UNI_CLIENT = CLIENT_.iloc[1]
CLIENT = ROEY_UNI_CLIENT

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT[0], client_secret=CLIENT[1])
SPOTIFY = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getPlaylist(plalist_id: str):
    SPOTIFY.trace = False
    playlist = SPOTIFY.playlist(plalist_id)
    songs = playlist["tracks"]["items"]
    ids = []
    for i in range(len(songs)):
        ids.append(songs[i]["track"]["id"])
    return ids


def getPlaylistAudioFeatures(ids):  # , genre: str):
    features = SPOTIFY.audio_features(ids)
    df = pd.DataFrame(features)
    # df.insert(loc=len(df.columns), column=genre, value="1")
    # print(df.to_string())
    return df

# def getPlaylistData(plalist_id: str, genre: str):
#     client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT[0], client_secret=CLIENT[1])
#     spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#     spotify.trace = False
#     playlist = spotify.playlist(plalist_id)
#     songs = playlist["tracks"]["items"]
#     ids = []
#     for i in range(len(songs)):
#         ids.append(songs[i]["track"]["id"])
#     features = spotify.audio_features(ids)
#     df = pd.DataFrame(features)
#     df.insert(loc=len(df.columns), column=genre, value="1")
#     print(df.to_string())
