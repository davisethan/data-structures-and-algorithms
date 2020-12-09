import unittest
from magic_index import magic_index

class TestMagicIntdex(unittest.TestCase):
  def test_magic_index(self):
    # (integers, expected)
    cases = [
      ([0, 2, 3, 4, 5], 0),
      ([-2, 1, 3, 4, 5], 1),
      ([-2, -1, 0, 1, 4], 4),
      ([-2, -1, 0, 3, 6], 3),
      ([2, 3, 4, 5, 6], -1),
      ([-2, -1, 0, 1, 2], -1),
    ]
    for case in cases:
      with self.subTest(case):
        self.assertEqual(case[1], magic_index(case[0]))

if __name__ == "__main__":
  unittest.main()
