import Track
from GetSpotifyData import *
from Track import *


class Songs:
    def __init__(self):
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

    def __str__(self):
        st = ""
        for t in self._songs.values():
            st += str(t) + "\n"
        return st
