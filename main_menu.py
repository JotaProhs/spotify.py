from artist import Artist
from artist_menu import ArtistMenu
from cross_module_functions import CrossModuleDef
from input import InputHandler
from song import Song
from song_menu import SongMenu


class MainMenu:
    def __init__(self, user):
        self.user = user
        self.chosen_song = None
        self.chosen_artist = None
        self.choices = {
            "1": self.search_song,
            "2": self.search_artist,
            "3": self.view_user_profile,
            "4": self.quit,

        }

    @staticmethod
    def display_main_menu_options():
        print("\nChoose an option from the following menu:")
        print("1. Search Song.\n"
              "2. Search Artist.\n"
              "3. View My Profile.\n"
              "4. Quit.\n"
              )

    def run_main_menu(self):
        main_menu_active = True
        while main_menu_active:
            self.display_main_menu_options()
            choice = InputHandler.get_choice("\nEnter your choice: -->  ", self.choices.keys())
            action = self.choices.get(choice)
            if action:
                action()
                if action == self.search_song and self.chosen_song:
                    song_menu = SongMenu(self.chosen_song, self.user)
                    song_menu.run_song_menu()
                    main_menu_active = False

                elif action == self.search_artist and self.chosen_artist:
                    artist_menu = ArtistMenu(self.chosen_artist, self.user)
                    artist_menu.run_artist_menu()

    def search_song(self):
        song_from_user = InputHandler.get_text_input("Write the name of the song: -->  ")
        self.chosen_song = Song.search_song_and_display_info(song_from_user)

    def search_artist(self):
        artist_from_user = InputHandler.get_text_input("Write the name of the artist: -->  ")
        self.chosen_artist = Artist.search_artist(artist_from_user)
        if self.chosen_artist:
            self.chosen_artist.print_artist_name()
            self.chosen_artist.display_popular_songs()
            self.chosen_artist.display_discography()
            self.chosen_artist.display_similar_artists()
            self.chosen_artist.display_artist_info()
        return

    def view_user_profile(self):
        self.user.view_user_profile()

    @staticmethod
    def quit():
        CrossModuleDef.quit()



