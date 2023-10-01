from testData import songsData
from Song import Song
from Playlist import Playlist
from typing import Literal


def generateDummyData():
    songs = getDefaultSongs()
    pl1 = Playlist("playlist1")
    # pl2 = Playlist("playlist2")
    pl1.addSong(songs[0])
    pl1.addSong(songs[1])


def getDefaultSongs() -> list[Song]:
    songs: list[Song] = []
    for song in songsData:
        mySong = Song(**song)
        songs.append(mySong)
    return songs


def lastTwoOptions(menu: dict[int, str]):

    # option for adding return to previous menu
    # prevMenuOption = len(menu.keys()) + 1
    # menu[prevMenuOption] = "Return to previous Menu"

    mainMenuOption = 0
    menu[mainMenuOption] = "Return to Main Menu"

    return menu


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
        except Exception as e:
            # print(e)
            print("Invalid input, try again!!")


def validatePlaylistName(name) -> bool:
    for d in Playlist.getAllPLaylists():
        if d['name'].lower() == name.lower():
            separator()
            print("Playlist with that name already exists, Try again!")
            return True
    return False


def getPlaylistFromUser() -> Playlist | Literal[False]:
    playlists = Playlist.getAllPLaylists()
    if (len(playlists) == 0):
        separator()
        print("No playlist found!")
        return
    # create menu
    playlistMenu = {i+1: pl['name'] for i, pl in enumerate(playlists)}
    playlistMenu = lastTwoOptions(playlistMenu)

    choice = getUserChoice(playlistMenu, "Playlists")
    if (choice == 0):
        return False

    # get that playlist
    for x in playlists:
        if (x['name'] == playlistMenu[choice]):
            return x['object']
    return False


def getSongFromUser() -> Song | Literal[False]:
    songs = getDefaultSongs()
    if (len(songs) == 0):
        separator()
        print("No Songs found in the list!")
        return
    # create menu
    songsMenu = {i+1: s.title for i, s in enumerate(songs)}
    songsMenu = lastTwoOptions(songsMenu)

    choice = getUserChoice(songsMenu, "Songs")
    if (choice == 0):
        return False

    # get that Song
    for x in songs:
        if (x.title == songsMenu[choice]):
            return x
    return False


def getPlaylistsSongsFromUser(playlist: Playlist) -> Song | Literal[False]:
    songs = playlist.songs
    if (len(songs) == 0):
        separator()
        print("No Songs found in the list!")
        return

    # create menu
    songsMenu = {i+1: s.title for i, s in enumerate(songs)}
    songsMenu = lastTwoOptions(songsMenu)

    choice = getUserChoice(songsMenu, "Songs")
    if (choice == 0):
        return False

    # get that Song
    for x in songs:
        if (x.title == songsMenu[choice]):
            return x
    return False
