from testData import songsData
from Song import Song
from Playlist import Playlist


def getDefaultSongs() -> list[Song]:
    songs: list[Song] = []
    for song in songsData:
        mySong = Song(**song)
        songs.append(mySong)
    return songs


def separator() -> None:
    print("-"*20)


def getUserChoice(options: dict[int, str], optionTitle: str = "") -> int:
    """ Docstring """
    separator()
    print("Select an option", end=" ")
    if (optionTitle != ""):
        print("from", optionTitle, end="")
    print(":")
    separator()
    for opt in options:
        print(opt, ":", options[opt])
    while True:
        try:
            inp = int(input("Your Choice: "))
            if (inp not in options.keys()):
                raise Exception("Invalid input")
            return inp
        except:
            print("Invalid input, try again!")

def validatePlaylistName(name) -> bool:
    for d in Playlist.playlists:
        if d['name'].lower() == name.lower():
            print("Playlist with that name already exists, Try again!")
            return True
    return False

def selectPlaylist() -> object:
    choice = getUserChoice({i+1: d['name'] for i, d in enumerate(Playlist.playlists)} \
                            | {00: "Return to previous menu", 0: "Exit"}, " Playlists")
    print(choice)
    
    return