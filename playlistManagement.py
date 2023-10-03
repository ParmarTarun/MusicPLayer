from Playlist import Playlist
from utility import *


def performAddSong(playlist: Playlist) -> None:
    """Driver function for adding song to playlist"""
    song = getSongFromUser()
    if (song):
        if (song.title in playlist.getAllSongsName()):
            separator()
            print("Song already in the playlist!")
        else:
            playlist.addSong(song)
    return None


def performRmoveSong(playlist: Playlist) -> None:
    """Driver function for removing song to playlist"""
    if (len(playlist.songs) > 0):
        song = getPlaylistsSongsFromUser(playlist)
        if (song):
            if (song not in playlist.songs):
                separator()
                print("Song not in the playlist!")
            playlist.removeSong(song)
    else:
        print("No Songs found in the playlist!")
    return None


def performDisplaySongs(playlist: Playlist):
    """Driver function for displayin songs in playlist"""
    songs = playlist.songs
    if (len(songs) > 0):
        separator()
        print("Songs in", playlist.name)
        for s in songs:
            print(s.title)
    else:
        separator()
        print("No Songs found in the playlist!")
