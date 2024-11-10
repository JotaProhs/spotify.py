from artist import Artist
from art_final import logo
from input import InputHandler
from main_menu import MainMenu
from song import Song
from user import UserProfile


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
