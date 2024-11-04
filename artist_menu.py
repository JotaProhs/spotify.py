from input import InputHandler
from cross_module_functions import CrossModuleDef


class ArtistMenu:

    def __init__(self, chosen_artist, user):
        self.chosen_artist = chosen_artist
        self.user = user
        self.choices = {
            "1": self.follow_artist,
            "2": self.like_artist,
            "3": self.play_artist_songs_randomly,
            "4": self.go_back_to_main_memu,
            "5": self.quit,
        }

    @staticmethod
    def display_main_menu_options():
        print("\nChoose an option from the following menu:")
        print("1. Follow Artist.\n"
              "2. Like Artist.\n"
              "3. Play Artist Songs Randomly.\n"
              "4. Go Back to Main Menu.\n"
              "5. Quit.\n"
              )

    def run_artist_menu(self):
        artist_menu_active = True
        while artist_menu_active:
            self.display_main_menu_options()
            choice = InputHandler.get_choice("\nEnter your choice: -->  ", self.choices.keys())
            action = self.choices.get(choice)
            if action:
                action()

    def follow_artist(self):
        self.chosen_artist.follow_artist()

    def like_artist(self):
        self.chosen_artist.like_artist()

    def go_back_to_main_memu(self):
        cross_module_def = CrossModuleDef(self.user)
        cross_module_def.go_back_to_main_memu()

    def play_artist_songs_randomly(self):
        self.chosen_artist.play_artist_songs_randomly()

    @staticmethod
    def quit():
        CrossModuleDef.quit()
