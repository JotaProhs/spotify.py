from song import Song
from art_final import song_playing_art
import random
import json
import time


class Artist:
    artists = []
    chosen_artist = None
    _filename = "data.json"

    def __init__(self, artist_name, albums, monthly_listeners, followers,
                 likes, similar_artists, first_album_release, featuring_albums, user):
        self.artist_name = artist_name
        self.albums = albums
        self.monthly_listeners = monthly_listeners
        self.followers = followers
        self.likes = likes
        self.similar_artists = similar_artists
        self.first_album_release = first_album_release
        self.featuring_albums = featuring_albums
        self.user = user
        self.popular_songs = []

    @classmethod
    def instantiate_artists_from_json(cls, user):
        with open(cls._filename, 'r') as file:
            data = json.load(file)

        for artist in data:
            artist_instance = Artist(
                artist_name=artist['artist_name'],
                albums=artist['albums'],
                monthly_listeners=artist['monthly_listeners'],
                followers=artist['followers'],
                likes=artist['likes'],
                similar_artists=artist['similar_artists'],
                first_album_release=artist['first_album_release'],
                featuring_albums=artist["featured"],
                user=user
            )

            for song in Song.songs:
                if song.artist_name == artist_instance.artist_name:
                    artist_instance.popular_songs.append(song)

            cls.artists.append(artist_instance)

        return cls.artists

    @classmethod
    def search_artist(cls, artist_from_user):
        artist_found = False
        for artist in cls.artists:
            if artist_from_user.lower() in artist.artist_name.lower():
                cls.chosen_artist = artist
                return cls.chosen_artist

        if not artist_found:
            print(f"No artist matched the input '{artist_from_user}'.")
            return None

    @staticmethod
    def format_number_with_commas(number):
        return f"{number:,}"

    def print_artist_name(self):
        print(f"\n{self.artist_name.title()}:\n"
              f"{Artist.format_number_with_commas(self.monthly_listeners)} monthly listeners.\n"
              f"{Artist.format_number_with_commas(self.followers)} followers.\n"
              f"{Artist.format_number_with_commas(self.likes)} likes.")

    def display_popular_songs(self):
        def get_play_count(song_object):
            return song_object.played

        self.popular_songs.sort(key=get_play_count, reverse=True)

        print("\nPopular Songs")
        for song in self.popular_songs:
            print(f"{song.song_name.title()} - Played {song.played} times.")

    def display_discography(self):
        print("\nDiscography:")
        for i, album in enumerate(self.albums, start=1):
            print(f"{i}. {album["album_name"].title()} - {album["album_year"]}")

    def display_featuring_albums(self):
        print(f"\nFeaturing {self.artist_name}:")
        for i, album in enumerate(self.featuring_albums, start=1):
            print(f"{i}. Album: {album["album_name"]}\n"
                  f"Description: {album["description"]}")

    def display_similar_artists(self):
        print("\nFans also like:")
        for i, artist in enumerate(self.similar_artists, start=1):
            print(f"{i}. {artist.title()}")

    def display_artist_info(self):
        print("\nAbout the artist:")
        print(f"{self.artist_name.title()} is a band or an artist who "
              f"released their first album in {self.first_album_release}. "
              f"They currently have {Artist.format_number_with_commas(self.monthly_listeners)} monthly "
              f"listeners and {Artist.format_number_with_commas(self.followers)} followers.")

    def follow_artist(self):
        if self in self.user.followed_artists:
            print(f"You are already following "
                  f"{self.artist_name.title()}")

        else:
            self.user.followed_artists.append(self)
            self.user.following += 1
            self.followers += 1
            print(f"You are now following {self.artist_name.title()} - Total followers: "
                  f"{Artist.format_number_with_commas(self.followers)}.")

    def like_artist(self):
        if self in self.user.liked_artists:
            print(f"You have already liked {self.artist_name.title()}")

        else:
            self.user.liked_artists.append(self)

            self.likes += 1
            print(f"You have liked {self.artist_name.title()} - Total likes: "
                  f"{Artist.format_number_with_commas(self.likes)}.")

    def play_artist_songs_randomly(self):
        random.shuffle(self.popular_songs)
        for song in self.popular_songs:
            print(song_playing_art)
            print(f"Now playing {song.song_name.title()} by {song.artist_name.title()}.")
            time.sleep(2)

