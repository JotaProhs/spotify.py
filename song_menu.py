from cross_module_functions import CrossModuleDef
from input import InputHandler


class SongMenu:

    def __init__(self, chosen_song, user):
        self.chosen_song = chosen_song
        self.user = user
        self.choices = {
            "1": self.play_song,
            "2": self.like_song,
            "3": self.add_song_to_playlist,
            "4": self.go_back_to_main_memu,
            "5": self.quit,
        }

    @staticmethod
    def display_main_menu_options():
        print("\nChoose an option from the following menu:")
        print("1. Play Song.\n"
              "2. Like Song.\n"
              "3. Add Song to Playlist.\n"
              "4. Go Back to Main Menu.\n"
              "5. Quit.\n"
              )

    def run_song_menu(self):
        artist_menu_active = True
        while artist_menu_active:
            self.display_main_menu_options()
            choice = InputHandler.get_choice("\nEnter your choice: -->  ", self.choices.keys())
            action = self.choices.get(choice)
            if action:
                action()

    def play_song(self):
        self.chosen_song.play_song()

    def like_song(self):
        self.chosen_song.like_song()

    def add_song_to_playlist(self):
        self.chosen_song.add_song_to_playlist()

    def go_back_to_main_memu(self):
        cross_module_def = CrossModuleDef(self.user)
        cross_module_def.go_back_to_main_memu()

    @staticmethod
    def quit():
        CrossModuleDef.quit()

