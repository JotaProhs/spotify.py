from artist import Artist
from song import Song
from user import UserProfile
from main_menu import MainMenu
from input import InputHandler
from art_final import logo


def main():
    print(f"Welcome to {logo}")
    name = InputHandler.get_text_input("Write your name: -->  ")
    user = UserProfile(name)
    user.greet_user()

    Song.instantiate_song_from_json(user)
    Artist.instantiate_artists_from_json(user)
    main_menu = MainMenu(user)
    main_menu.run_main_menu()


if __name__ == "__main__":
    main()

