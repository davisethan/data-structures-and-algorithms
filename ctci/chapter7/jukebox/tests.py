import unittest
from collections import deque
from Bank import Bank, Quarter, Dime, Nickel, Penny
from Music import Music, Track, MissingTrackException

class TestBank(unittest.TestCase):
    def test_bank_has_enough(self):
        # (case name, coins, expected)
        cases = [
            ("too_little", (Dime, Dime), False),
            ("exact_amount", (Quarter,), True),
            ("more_than_enough", (Dime, Dime, Dime), True),
        ]
        for case in cases:
            with self.subTest(case[0]):
                bank = Bank()
                queue = deque(case[1])
                bank.add_coins(queue)
                self.assertEqual(case[2], bank.has_enough())

    def test_bank_take_enough(self):
        # (case name, coins, expected remainder coins)
        cases = [
            ("remainder_coins", (Quarter, Nickel), (Nickel,)),
            ("no_remainder_coins", (Dime, Dime, Dime), tuple()),
        ]
        for case in cases:
            with self.subTest(case[0]):
                bank = Bank()
                queue = deque(case[1])
                bank.add_coins(queue)
                bank.take_enough()
                self.assertEqual(case[2], tuple(coin for coin in bank.get_coins()))

class TestMusic(unittest.TestCase):
    def test_music_select_track_by_id(self):
        tracks = {
            "a0": Track("a0", "Like a Rolling Stone", "", "Bob Dylan"),
            "b2": Track("b3", "I Can't Get No Satisfaction", "", "Rolling Stones"),
            "c1": Track("c1", "Imagine", "", "John Lennon"),
            "d3": Track("d3", "What's Going On", "", "Marvin Gaye")
        }
        music = Music(tracks)
        # (case name, track id, expected track string)
        cases = [
            ("select track by id", "c1", "Imagine--John Lennon"),
        ]
        for case in cases:
            with self.subTest(case[0]):
                track = music.select_track_by_id(case[1])
                self.assertEqual(case[2], str(track))

    def test_music_select_track_by_id_with_exception(self):
        tracks = {
            "a0": Track("a0", "Like a Rolling Stone", "", "Bob Dylan"),
            "b2": Track("b3", "I Can't Get No Satisfaction", "", "Rolling Stones"),
            "c1": Track("c1", "Imagine", "", "John Lennon"),
            "d3": Track("d3", "What's Going On", "", "Marvin Gaye")
        }
        music = Music(tracks)
        with self.assertRaises(MissingTrackException):
            music.select_track_by_id("z9")

if __name__ == "__main__":
    unittest.main()
