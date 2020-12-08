import unittest
from towers_of_hanoi import towers_of_hanoi

class TestTowersOfHanoi(unittest.TestCase):
    def test_towers_of_hanoi(self):
        # (Disks at start, Disks at end)
        cases = [
            (([1], [], []), ([], [], [1])),
            (([2, 1], [], []), ([], [], [2, 1])),
            (([3, 2, 1], [], []), ([], [], [3, 2, 1])),
            (([4, 3, 2, 1], [], []), ([], [], [4, 3, 2, 1])),
            (([5, 4, 3, 2, 1], [], []), ([], [], [5, 4, 3, 2, 1])),
        ]
        for case in cases:
            towers = case[0]
            towers_of_hanoi(towers)
            self.assertEqual(case[1], towers)

if __name__ == "__main__":
    unittest.main()
