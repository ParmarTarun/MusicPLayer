from testData import songsData
from Song import Song

menu = {
    1: "Checkout default Songs",
    0: "Exit"
}


def getDefaultSongs() -> list[Song]:
    songs: list[Song] = []
    for song in songsData:
        mySong = Song(**song)
        songs.append(mySong)
    return songs


def separator() -> None:
    print("-"*20)


def getUserChoice(options: dict[int, str], optionTitle: str = "") -> int:
    """"""
    separator()
    print("Select an option", end=" ")
    if (optionTitle != ""):
        print("from", optionTitle, end="")
    print(":")
    separator()
    for opt in options:
        print(opt, ":", menu[opt])
    while True:
        try:
            inp = int(input("Your Choice: "))
            if (inp not in menu.keys()):
                raise Exception("Invalid input")
            if (inp == 0):
                return -1
            return inp
        except:
            print("Invalid input, try again!")
