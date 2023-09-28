import sys

from Player import Player
from Song import Song
from Playlist import Playlist

from playlistManagement import *
from utility import *

menu = {
    1: "Create Playlist",
    2: "Manage Playlist",
    # 3: "Play Playlist",
    0: "Exit"
}

managePlaylistMenu = {
    1: "Display Songs",
    2: "Add song",
    3: "Remove song",
}


def performPlaylistManagement(playlist: Playlist) -> None:

    choice = getUserChoice(managePlaylistMenu, f"menu for {playlist.name}")
    if choice == 1:
        performDisplaySongs(playlist)
    if choice == 2:
        performAddSong(playlist)
    elif choice == 3:
        performRmoveSong(playlist)
    else:
        return None


def performCreatePlaylist() -> None:
    name = input("Enter name for the Playlist: ")
    exists = validatePlaylistName(name)
    if not exists:
        playlist = Playlist(name)
        print(f"Playlist {playlist.name} created!")


# generateDummyData()
print("Welcome to the world of music")
while True:
    choice = getUserChoice(menu, "Main Menu")
    if choice == 1:
        performCreatePlaylist()

    elif choice == 2:
        playlist = getPlaylistFromUser()
        if (playlist):
            performPlaylistManagement(playlist)

    elif (choice == 0):
        break
