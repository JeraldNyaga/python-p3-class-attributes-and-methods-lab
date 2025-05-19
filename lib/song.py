class Song:
    genre_count = {}
    artist_count ={}
    artists = []
    genres = []
    count = 0
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist  
        self.genre = genre
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.add_to_genre_count(genre)
        if genre not in cls.genres:
            cls.genres.append(genre)

            
    @classmethod
    def add_to_artists(cls, artist):
        cls.add_to_artist_count(artist)
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
