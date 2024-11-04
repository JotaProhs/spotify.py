from art_final import song_playing_art
import time


class UserProfile:

    def __init__(self, name):
        self.name = name
        self.followers = 0
        self.following = 0
        self.liked_songs = []
        self.liked_artists = []
        self.followed_artists = []
        self.playlist = []

    def greet_user(self):
        print(f"\nWelcome {self.name.capitalize()}")

    def view_user_profile(self):
        print(f"{self.name.title()}'s Profile:")
        self.display_followers()
        self.display_following()
        self.display_liked_songs()
        self.display_liked_artists()
        self.display_followed_artists()
        self.display_playlist()

    def display_followers(self):
        print(f"You have {self.followers} followers.")

    def display_following(self):
        print(f"You are following {self.following} artist/s.")

    def display_liked_songs(self):
        print("\nSongs you like:")
        for i, song in enumerate(self.liked_songs, start=1):
            print(f"{i}. {song.song_name.title()} by {song.artist_name.title()}.")

    def display_liked_artists(self):
        print("\nArtists you like:")
        for i, artist in enumerate(self.liked_artists, start=1):
            print(f"{i}. {artist.artist_name.title()}.")

    def display_followed_artists(self):
        print("\nArtists you follow:")
        for i, artist in enumerate(self.followed_artists, start=1):
            print(f"{i}. {artist.artist_name.title()}")

    def display_playlist(self):
        print("\nYour playlists contains:")
        for i, song in enumerate(self.playlist, start=1):
            print(f"{i}. {song.song_name.title()} by {song.artist_name.title()}")

    def play_playlist(self):
        print(song_playing_art)
        for song in self.playlist:
            print(f"Now playing {song.song_name.title()} by {song.artist_name.title()}.")
            time.sleep(2)


