import unittest
from power_set import power_set

class TestPowerSet(unittest.TestCase):
  def test_power_set(self):
    # (set, power_set)
    cases = [
      (set(), (set(),)),
      ({1}, (set(), {1},)),
      ({1, 2}, (set(), {1}, {2}, {1, 2},)),
      ({1, 2, 3}, (set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3},))
    ]
    for case in cases:
      with self.subTest(case):
        expected = {frozenset(lot) for lot in case[1]}
        self.assertEqual(expected, power_set(case[0]))

if __name__ == "__main__":
  unittest.main()
