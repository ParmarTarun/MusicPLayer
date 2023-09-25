from Player import Player
from Song import Song
from Playlist import Playlist
from utility import getUserChoice, menu


inp = ""
print("Welcome to the world of music")
while True:
    choice = getUserChoice(menu, "main menu")
    if (choice == -1):
        break
