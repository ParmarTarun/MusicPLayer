from Player import Player
from Song import Song
from Playlist import Playlist
from utility import getUserChoice, validatePlaylistName, selectPlaylist
import sys

menu = {
    1: "Create Playlist",
    2: "Manage Playlist",  # 1. Add song, 2. Remvove Song
    3: "Play Playlist",
    0: "Exit"
}

managePlaylistMenu = {
    1: "Add song",
    2: "Remove song",
    3: "Return to Main Menu",
    0: "Exit"
}


def managePlaylist() -> None:
    while True:
        choice = getUserChoice(managePlaylistMenu, "Manage Playlist menu")
        if choice == 1:
            print('in 1')
        elif choice == 2:
            print('in 2')
        elif choice == 3:
            break
        elif choice == 0:
            sys.exit()


def performCreatePlaylist():
    name = input("Enter name for the Playlist: ")
    exists = validatePlaylistName(name)
    if not exists:
        playlist = Playlist(name)
        print(f"Playlist {playlist.name} created!")


print("Welcome to the world of music")
while True:
    choice = getUserChoice(menu, "Main Menu")
    if choice == 1:
        performCreatePlaylist()

    elif choice == 2:
        playlist = selectPlaylist()
        # managePlaylist()

    elif (choice == 0):
        break
