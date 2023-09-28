from Song import Song


class Playlist:
    __playlists = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.songs: list[Song] = []
        Playlist.__playlists.append({'object': self, 'name': name})

    @classmethod
    def getAllPLaylists(cls):
        playlists = cls.__playlists.copy()
        return playlists

    def getAllSongsName(self):
        names = []
        for s in self.songs:
            names.append(s.title)
        return names

    def addSong(self, song: Song):
        self.songs.append(song)

    def removeSong(self, song: Song):
        if (song in self.songs):
            self.songs.remove(song)
