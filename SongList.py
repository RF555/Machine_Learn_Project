import Track
from GetSpotifyData import *
from Track import *
import csv


class SongList:
    def __init__(self):
        self.csv = open('spo.csv', 'w', encoding='UTF8', newline='')
        self.header = []
        self.header.append('danceability')
        self.header.append('energy')
        self.header.append('key')
        self.header.append('loudness')
        self.header.append('speechiness')
        self.header.append('acousticness')
        self.header.append('instrumentalness')
        self.header.append('liveness')
        self.header.append('valence')
        self.header.append('tempo')
        self.header.append('duration_ms')
        self.header.append('genre')
        self.writer = csv.writer(self.csv)
        self.writer.writerow(self.header)
        self._songs = {}

    def add_playlist(self, plalist_id: str, genre: str):

        playlist = getPlaylist(plalist_id)
        playlist_features = getPlaylistAudioFeatures(playlist).to_dict('index')
        for t in playlist_features.values():
            if t.get("id") in self._songs:
                self._songs.get(t.get("id")).update_genre(genre)
            else:
                track = Track(t, genre)
                self._songs.update({track.id: track})
                data = []
                for val in self.header:
                    data.append(getattr(track, val))
                self.writer.writerow(data)

    def __str__(self):
        st = ""
        for t in self._songs.values():
            st += str(t) + "\n"
        return st
