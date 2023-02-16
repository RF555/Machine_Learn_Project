import csv
import pandas as pd
from Songs import *


header = ['danceability', 'energy', 'key', 'loudness','speechiness','acousticness','instrumentalness'
          'liveness','tempo']


with open('spo.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    # writer.writerow(data)
    ROCK_MIX = "37i9dQZF1EQpj7X7UK8OOF"

    songs = Songs()
    songs.add_playlist(ROCK_MIX, "ROCK")
    a = pd.DataFrame()
    print(songs)
