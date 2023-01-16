from GetSpotifyData import SPOTIFY


class Track:
    _audio_analysis = None

    def __int__(self, audio_features: dict, genre: str):
        self._id = audio_features.get("id")
        self._danceability = audio_features.get("danceability")
        self._energy = audio_features.get("energy")
        self._key = audio_features.get("key")
        self._loudness = audio_features.get("loudness")
        self._mode = audio_features.get("mode")
        self._speechiness = audio_features.get("speechiness")
        self._acousticness = audio_features.get("acousticness")
        self._instrumentalness = audio_features.get("instrumentalness")
        self._liveness = audio_features.get("liveness")
        self._valence = audio_features.get("valence")
        self._tempo = audio_features.get("tempo")
        self._type = audio_features.get("type")
        self._duration_ms = audio_features.get("duration_ms")
        self._time_signature = audio_features.get("time_signature")

    def getAudioAnalysis(self):
        self._audio_analysis = SPOTIFY.audio_analysis("0PNt5WTw092eED0ru9SuIp")
