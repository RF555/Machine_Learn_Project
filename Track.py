from GetSpotifyData import SPOTIFY


class Track:

    def __init__(self, audio_features, genre):
        self.id = audio_features.get("id")
        self.danceability = audio_features.get("danceability")
        self.energy = audio_features.get("energy")
        self.key = audio_features.get("key")
        self.loudness = audio_features.get("loudness")
        self.mode = audio_features.get("mode")
        self.speechiness = audio_features.get("speechiness")
        self.acousticness = audio_features.get("acousticness")
        self.instrumentalness = audio_features.get("instrumentalness")
        self.liveness = audio_features.get("liveness")
        self.valence = audio_features.get("valence")
        self.tempo = audio_features.get("tempo")
        self.duration_ms = audio_features.get("duration_ms")
        self.time_signature = audio_features.get("time_signature")
        self.audio_analysis = None
        if genre == "ROCK":
            self.ROCK = 1
            self.genre = 1
        else:
            self.ROCK = 0
        if genre == "FOLK_ACUSTIC":
            self.FOLK_ACUSTIC = 1
            self.genre = 2
        else:
            self.FOLK_ACUSTIC = 0
        if genre == "POP":
            self.POP = 1
            self.genre = 3
        else:
            self.POP = 0

        if genre == "METAL":
            self.METAL = 1
            self.genre = 4
        else:
            self.METAL = 0
        if genre == "HIP_HOP":
            self.genre = 5
            self.HIP_HOP = 1
        else:
            self.HIP_HOP = 0
        if genre == "COUNTRY":
            self.genre = 6
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
        self.audio_analysis = SPOTIFY.audio_analysis("0PNt5WTw092eED0ru9SuIp")

    def __str__(self):
        return str("details of id: " + self.id + "\n\t\tGenere: ROCK=" + str(self.ROCK) + ", FOLK_ACUSTIC=" + str(
            self.FOLK_ACUSTIC) + ", " "POP=" + str(self.POP) + ", METAL=" + str(self.METAL) + ", HIP_HOP=" + str(
            self.HIP_HOP) + ", COUNTRY=" + str(self.COUNTRY) + "\n\t\tdanceability: " + str(
            self.danceability) + ",\n\t\tenergy: " + str(self.energy) + ",\n\t\tkey: " + str(
            self.key) + ",\n\t\tloudness: " + str(self.loudness) + ",\n\t\tmode: " + str(
            self.mode) + ",\n\t\tspeechiness: " + str(self.speechiness) + ",\n\t\tacousticness: " + str(
            self.acousticness) + ",\n\t\tinstrumentalness: " + str(
            self.instrumentalness) + ",\n\t\tliveness: " + str(self.liveness) + ",\n\t\tvalence: " + str(
            self.valence) + ",\n\t\ttempo: " + str(self.tempo) + ",\n\t\tduration_ms: " + str(
            self.duration_ms) + ",\n\t\ttime_signature: " + str(self.time_signature) + "\n\n")

