from GetSpotifyData import SPOTIFY


class Track:

    def __init__(self, audio_features, genre):
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
        self._duration_ms = audio_features.get("duration_ms")
        self._time_signature = audio_features.get("time_signature")
        self._audio_analysis = None
        if genre == "ROCK":
            self.ROCK = 1
        else:
            self.ROCK = 0
        if genre == "FOLK_ACUSTIC":
            self.FOLK_ACUSTIC = 1
        else:
            self.FOLK_ACUSTIC = 0
        if genre == "POP":
            self.POP = 1
        else:
            self.POP = 0

        if genre == "METAL":
            self.METAL = 1
        else:
            self.METAL = 0
        if genre == "HIP_HOP":
            self.HIP_HOP = 1
        else:
            self.HIP_HOP = 0
        if genre == "COUNTRY":
            self.COUNTRY = 1
        else:
            self.COUNTRY = 0

    def update_genre(self, genre):
        if genre == "ROCK":
            self.ROCK = 1
        if genre == "FOLK_ACUSTIC":
            self.FOLK_ACUSTIC = 1
        if genre == "POP":
            self.POP = 1
        if genre == "METAL":
            self.METAL = 1
        if genre == "HIP_HOP":
            self.HIP_HOP = 1
        if genre == "COUNTRY":
            self.COUNTRY = 1

    def getAudioAnalysis(self):
        self._audio_analysis = SPOTIFY.audio_analysis("0PNt5WTw092eED0ru9SuIp")

    def __str__(self):
        return str("details of id: " + self._id + "\n\t\tGenere: ROCK=" + str(self.ROCK) + ", FOLK_ACUSTIC=" + str(
            self.FOLK_ACUSTIC) + ", " "POP=" + str(self.POP) + ", METAL=" + str(self.METAL) + ", HIP_HOP=" + str(
            self.HIP_HOP) + ", COUNTRY=" + str(self.COUNTRY) + "\n\t\t_danceability: " + str(
            self._danceability) + ",\n\t\t_energy: " + str(self._energy) + ",\n\t\t_key: " + str(
            self._key) + ",\n\t\t_loudness: " + str(self._loudness) + ",\n\t\t_mode: " + str(
            self._mode) + ",\n\t\t_speechiness: " + str(self._speechiness) + ",\n\t\t_acousticness: " + str(
            self._acousticness) + ",\n\t\t_instrumentalness: " + str(
            self._instrumentalness) + ",\n\t\t_liveness: " + str(self._liveness) + ",\n\t\t_valence: " + str(
            self._valence) + ",\n\t\t_tempo: " + str(self._tempo) + ",\n\t\t_duration_ms: " + str(
            self._duration_ms) + ",\n\t\t_time_signature: " + str(self._time_signature) + "\n\n")

    @property
    def id(self):
        return self._id
