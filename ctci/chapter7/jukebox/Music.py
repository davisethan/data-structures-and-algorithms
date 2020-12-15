class Music:
    def __init__(self, tracks):
        self._tracks = tracks

    def select_track_by_id(self, id):
        if id not in self._tracks:
            raise MissingTrackException()
        return self._tracks[id]

class Track:
    def __init__(self, id, title, album, band):
        self._id = id
        self._title = title
        self._album = album
        self._band = band

    def __str__(self):
        return f"{self._title}-{self._album}-{self._band}"

class MissingTrackException(Exception):
    pass
