from time import sleep

from Playlist import Playlist
from Song import Song
from utility import separator
import progressbar
import keyboard


class Player:

    widgets = ['Progress:', progressbar.Bar(
        '#'), progressbar.Timer(format='%(elapsed)s')]
    bar = progressbar.ProgressBar(widgets=widgets)

    def __init__(self) -> None:
        self.currentDuration = 0
        self.currentSong = None
        self.__handlers = []
        self.options = {"p": ["pause", self.pauseSong],
                        "r": ["resume", self.resumeSong],
                        "s": ["stop", self.stopSong],
                        "n": ["next", self.nextSong]
                        }
        self.pause = False
        self.stop = False

    def __enablePlaybackOptions(self):
        for option in self.options.keys():
            handler = keyboard.add_word_listener(
                option, self.options[option][1], triggers=["enter"])
            self.__handlers.append(handler)

    def pauseSong(self):
        self.pause = True

    def resumeSong(self):
        pass

    def nextSong(self):
        self.currentDuration = self.currentSong.duration

    def stopSong(self):
        if (not self.pause):
            self.stop = True
            self.currentDuration = 0
            self.currentSong = None
            for _ in self.__handlers:
                item = self.__handlers.pop()
                try:
                    keyboard.remove_word_listener(item)
                except Exception:
                    pass

    def play(self, song: Song):
        self.currentSong = song
        self.currentDuration = 0
        while (song.duration != self.currentDuration):
            if (self.pause):
                inp = input("\nSong is paused... press r to resume\n")
                if (inp == 'r'):
                    self.pause = False
            elif (self.stop):
                break
            else:
                self.currentDuration += 0.1
                sleep(1)
                Player.bar.update(self.currentDuration)

    def playSong(self, song: Song):
        self.__enablePlaybackOptions()

        separator()
        print("Playing:", song.title, "by", ', '.join(song.artists))
        print("Playback options:", end=" ")
        for key in self.options.keys():
            print(f'{key}:{self.options[key][0]}', end=" | ")
        print()

        Player.bar.max_value = song.duration

        self.play(song)

    def playPlaylist(self, playlist: Playlist):
        self.__enablePlaybackOptions()
        for song in playlist.songs:
            separator()
            print("Playing:", song.title, "by", ', '.join(song.artists))

            print("Playback options:", end=" ")
            for key in self.options.keys():
                print(f'{key}:{self.options[key][0]}', end=" | ")
            print()

            Player.bar.max_value = song.duration

            self.play(song)
            if (self.stop):
                break
