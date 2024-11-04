import sys


class CrossModuleDef:

    def __init__(self, user):
        self.user = user

    def go_back_to_main_memu(self):
        from main_menu import MainMenu
        main_menu = MainMenu(self.user)
        main_menu.run_main_menu()

    @staticmethod
    def quit():
        print("Thank you for using Spotify.")
        sys.exit(0)
