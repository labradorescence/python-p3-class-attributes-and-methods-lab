class Song:

    count = 0
    genres = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_genres(genre)
        self.add_song_to_count()

    @classmethod
    def add_song_to_count(cls, plus_one=1):
        cls.count += plus_one

    @classmethod
    def add_to_genres(cls, this_song):
        cls.genres.append(this_song)

    @classmethod
    def genre_count()
    

    pass