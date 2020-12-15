from Bank import Bank, Coin
from Music import Music, MissingTrackException

class Jukebox:
    def __init__(self, tracks):
        self._bank = Bank()
        self._music = Music(tracks)

    def take_coins(coins):
        self._bank.add_coins(coins)

    def return_coins():
        return self._bank.remove_coins()

    def select_track_by_id(id):
        if self._bank.has_enough():
            self._bank.take_enough()
            self._music_select_track_by_id(id)

    def _music_select_track_by_id(self, id):
        try:
            track = self._music.select_track_by_id(id)
            print(track)
        except MissingTrackException:
            print(f"No track for id {id}")
