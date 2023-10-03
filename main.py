from Player import Player
from Song import Song
from Playlist import Playlist
from playlistManagement import *
from utility import *

menu = {
    1: "Create Playlist",
    2: "Manage Playlist",
    3: "Play a Song",
    4: "Play a Playlist",
    0: "Exit"
}

managePlaylistMenu = {
    1: "Display Songs",
    2: "Add song",
    3: "Remove song",
}


def performPlayPlaylist(playlist: Playlist):
    """Creates Player object and calls playPlaylist function with recieved playlist"""
    player = Player()
    player.playPlaylist(playlist)


def performPlaySong(song: Song):
    """Creates Player object and calls playSong function with recieved song"""
    player = Player()
    player.playSong(song)


def performPlaylistManagement(playlist: Playlist) -> None:
    """Takes users choice on particular playlist and calls the corresponding function for thst choice"""
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
    """Takes user input and creates new playlist with validation"""
    name = input("Enter name for the Playlist: ")
    exists = validatePlaylistName(name)
    if not exists:
        playlist = Playlist(name)
        print(f"Playlist {playlist.name} created!")


# generateDummyData()                       # call this function to auto populate some data
if __name__ == "__main__":
    print("Welcome to the world of music")
    while True:
        choice = getUserChoice(menu, "Main Menu")
        if choice == 1:
            performCreatePlaylist()

        elif choice == 2:
            playlist = getPlaylistFromUser()
            if (playlist):
                performPlaylistManagement(playlist)

        elif choice == 3:
            song = getSongFromUser()
            if (song):
                performPlaySong(song)

        elif choice == 4:
            playlist = getPlaylistFromUser()
            if (playlist):
                performPlayPlaylist(playlist)

        elif (choice == 0):
            break
