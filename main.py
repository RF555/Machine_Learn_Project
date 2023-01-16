import json

from GetSpotifyData import *
import pandas as pd

Roey_playlist = "78JTO1LbTGeD4kF8ACBQsC"
Passenger_playlist = "74xMzIlaOD7cIIOL4wW4Bq"
Beatles_playlist = "4L21s7bRV7QcUq1YaPobwB"
Disney_mix_playlist = "6UycuQgQHbt0bpS4sat8xc"
Queen_Best_Of_playlist = "595cY5S1FpMpiEIWsk6dG7"

FOLK_ACUSTIC_MIX = "37i9dQZF1EQp62d3Dl7ECY"
POP_MIX = "37i9dQZF1EQncLwOalG3K7"
METAL_MIX = "37i9dQZF1EQpgT26jgbgRI"
ROCK_MIX = "37i9dQZF1EQpj7X7UK8OOF"
HIP_HOP_MIX = "37i9dQZF1EQnqst5TRi17F"
COUNTRY_MIX = "37i9dQZF1EQmPV0vrce2QZ"

if __name__ == '__main__':
    # getPlaylistData(ROCK_MIX,"rock")
    # ids=getPlaylist(ROCK_MIX)
    # getPlaylistAudioFeatures(ids,"rock")

    analysis_dict = SPOTIFY.audio_analysis("0PNt5WTw092eED0ru9SuIp")
    with open("0PNt5WTw092eED0ru9SuIp.json", "w") as outfile:
        json.dump(analysis_dict, outfile)
