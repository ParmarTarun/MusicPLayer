from time import sleep

from Playlist import Playlist
from Song import Song
from utility import separator
import progressbar


class Player:
    def __init__(self) -> None:
        self.currentDuration = 0

    def playSong(self, song: Song):
        separator()
        print("Playing:", song.title, "by", ', '.join(song.artists))
        print("Playback options: p:pause | r:resume | s:stop | n:next")
        self.currentDuration = 0

        widgets = ['Progress:', progressbar.Bar(
            '#'), progressbar.Timer(format='%(elapsed)s'), f'/{song.duration}']

        bar = progressbar.ProgressBar(
            max_value=song.duration, widgets=widgets).start()

        while self.currentDuration != song.duration:
            sleep(1)
            self.currentDuration += 0.1
            if (self.currentDuration > song.duration):
                break
            bar.update(self.currentDuration)
