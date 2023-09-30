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
        self.options = {"p": ["pause", self.pause],
                        "r": ["resume", self.resume],
                        "s": ["stop", self.stop]
                        }
        self.pause = False
        self.stop = False

    def __enablePlaybackOptions(self):
        for option in self.options.keys():
            handler = keyboard.add_word_listener(
                option, self.options[option][1], triggers=["enter"])
            self.__handlers.append(handler)

    def pause(self):
        self.pause = True

    def resume(self):
        pass

    def stop(self):
        self.stop = True
        self.currentDuration = 0
        self.currentSong = None
        for x in self.__handlers:
            keyboard.remove_word_listener(x)

    def play(self, song: Song):
        while (song.duration != self.currentDuration):
            if (self.pause):
                inp = input("\nSong is paused..., press r to resume\n")
                if (inp == 'r'):
                    self.pause = False

            elif (self.stop):
                self.stop = False
                break
            else:
                self.currentDuration += 0.1
                sleep(1)
                Player.bar.update(self.currentDuration)

    def playSong(self, song: Song):
        self.currentSong = song
        self.currentDuration = 0
        separator()
        print("Playing:", song.title, "by", ', '.join(song.artists))

        self.__enablePlaybackOptions()
        print("Playback options:", end=" ")
        for key in self.options.keys():
            print(f'{key}:{self.options[key][0]}', end=" | ")
        print()

        Player.bar.max_value = song.duration

        self.play(song)
