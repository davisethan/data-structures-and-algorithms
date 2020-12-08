import unittest
from permutations import permutations

class TestPermutations(unittest.TestCase):
    def test_permutations(self):
        # (Characters, All character permutations)
        cases = [
            ("a", {"a"}),
            ("ab", {"ab", "ba"}),
            ("abc", {"abc", "acb", "bac", "bca", "cab", "cba"}),
        ]
        for case in cases:
            self.assertEqual(case[1], permutations(case[0]))

if __name__ == "__main__":
    unittest.main()
