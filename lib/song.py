class Song:

    count = 0  #class attribute
    genres = [] #class attribute
    artists = [] #class attribute
    genre_count = {} #class attribute
    artist_count = {} #class attribute

    def __init__(self, name, artist, genre): #init instance method
        self.name = name  #instance variable
        self.artist = artist #instance variable
        self.genre = genre #instance variable
        self.add_song_to_count() #instance variable
        self.add_to_genres(genre) #instance variable
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod #class method
    def add_song_to_count(cls, plus_one=1):
        cls.count += plus_one

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
                cls.artist_count[artist] = 1

