from input import InputHandler
from cross_module_functions import CrossModuleDef


class UserMenu:

    def __init__(self, user):
        self.user = user
        self.choices = {
            "1": self.play_playlist,
            "2": self.go_back,
            "3": self.quit,

        }

    @staticmethod
    def display_user_menu_options():
        print("\nChoose an option from the following menu:")
        print("1. Play Playlist.\n"
              "2. Go Back.\n"
              "3. Quit.\n"
              )

    def run_artist_menu(self):
        artist_menu_active = True
        while artist_menu_active:
            self.display_user_menu_options()
            choice = InputHandler.get_choice("\nEnter your choice: -->  ",
                                             self.choices.keys())
            action = self.choices.get(choice)
            if action:
                action()

    def play_playlist(self):
        pass

    def go_back(self):
        pass

    @staticmethod
    def quit():
        CrossModuleDef.quit()
