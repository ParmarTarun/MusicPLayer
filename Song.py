class Song:
    def __init__(self, title: str, artists: list[str], duration: float, filepath: str) -> None:
        self.title = title
        self.artists = artists
        self.duration = duration
        self.filepath = filepath
