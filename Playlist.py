class Playlist:
    playlists = []
    def __init__(self, name: str) -> None:
        self.name = name
        Playlist.playlists.append({'object': self, 'name': name})
