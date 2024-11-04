import json
from art_final import song_playing_art


class Song:
    songs = []
    chosen_song = None
    _filename = "data.json"

    def __init__(self, song_name, album, genre, year,
                 played, likes, artist_name, user):
        self.song_name = song_name
        self.album = album
        self.genre = genre
        self.year = year
        self.played = played
        self.likes = likes
        self.artist_name = artist_name  # Store artist name for linking
        self.user = user

    @classmethod
    def instantiate_song_from_json(cls, user):
        """
        Load artists data from a JSON file and create Song objects for each song in 'popular_songs'.
        """
        with open(cls._filename, 'r') as file:
            data = json.load(file)

        for artist in data:
            for song in artist['popular_songs']:
                # Create a Song object for each song in the popular_songs list
                song_instance = Song(
                    song_name=song['song_name'],
                    album=song['album'],
                    genre=song['genre'],
                    year=song['year'],
                    played=song['played'],
                    likes=song['likes'],
                    artist_name=artist['artist_name'],  # Link song with the artist
                    user=user
                )
                cls.songs.append(song_instance)

        return cls.songs

    @classmethod
    def search_song_and_display_info(cls, song_from_user):
        song_found = False
        for song in cls.songs:
            if song_from_user.lower() in song.song_name.lower():
                print(f"{song.song_name.title()} by {song.artist_name.title()} is a song of the album "
                      f"named '{song.album.title()}' recorded in {song.year}.")
                song_found = True
                cls.chosen_song = song
                return cls.chosen_song

        if not song_found:
            print(f"There is no song that matched the input '{song_from_user}'.")

    def play_song(self):
        print(song_playing_art)
        print(f"Now playing {self.song_name.title()} by the {self.artist_name.title()}")

    def like_song(self):
        if self in self.user.liked_songs:
            print(f"You have already liked {self.song_name.title()} by {self.artist_name.title()}")

        else:
            self.likes += 1
            print(f"You have liked {self.song_name.title()} by {self.artist_name.title()}"
                  f" - Total likes: {self.likes}")
            self.user.liked_songs.append(self)

    def add_song_to_playlist(self):
        if self in self.user.playlist:
            print(f"{self.song_name.title()} by {self.artist_name.title()} "
                  f"is already in your playlist")

        else:
            self.user.playlist.append(self)
            print(f"{self.song_name.title()} by {self.artist_name.title()} "
                  f"has been added to your playlist.")

    def __repr__(self):
        return (f"{__class__.__name__}(song_name='{self.song_name}', artist='{self.artist_name}', "
                f"album='{self.album}', genre='{self.genre}', year='{self.year}', played='{self.played}', "
                f"likes='{self.likes}')")

