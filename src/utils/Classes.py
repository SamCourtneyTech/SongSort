


class Song:
    def __init__(self, mixing, genre, subgenre, tempo, mode, mood_of_lyrics, genre_spec = None):
        self.mixing = mixing
        self.genre = genre
        self.subgenre = subgenre
        self.tempo = tempo
        self.mode = mode
        self.mood_of_lyrics = mood_of_lyrics
        self.genre_spec = genre_spec


class User:
    def __init__(self, mixing, genre, subgenre, tempo, mode, mood_of_lyrics, genre_spec=None):
        self.mixing = mixing
        self.genre = genre
        self.subgenre = subgenre
        self.tempo = tempo
        self.mode = mode
        self.mood_of_lyrics = mood_of_lyrics
        self.genre_spec = genre_spec
