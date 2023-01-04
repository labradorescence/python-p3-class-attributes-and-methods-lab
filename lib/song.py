class Song:

    all = []

    count = 0


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_all(self)


    @classmethod
    def add_to_all(cls, this_song):
        cls.all.append(this_song)

    @classmethod
    def add_song_to_count(cls, plus_one=1):
        cls.count += plus_one



    
    pass
