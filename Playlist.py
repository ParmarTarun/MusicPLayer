from Song import Song


class Playlist:
    """Class responsible for creating and maintaining playlists"""
    __playlists = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.songs: list[Song] = []
        Playlist.__playlists.append({'object': self, 'name': name})

    @classmethod
    def getAllPLaylists(cls):
        """retunrs all the playlists instances created"""
        playlists = cls.__playlists.copy()
        return playlists

    def getAllSongsName(self):
        """returns all the song names in a playlist"""
        names = []
        for s in self.songs:
            names.append(s.title)
        return names

    def addSong(self, song: Song):
        """add songs to playlist """
        self.songs.append(song)

    def removeSong(self, song: Song):
        """remove songs fron the playlist """
        if (song in self.songs):
            self.songs.remove(song)
