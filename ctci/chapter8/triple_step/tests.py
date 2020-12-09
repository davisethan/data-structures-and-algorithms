import unittest
from triple_step import triple_step

class TestTripleStep(unittest.TestCase):
  def test_triple_step(self):
    # (steps, solutions)
    cases = [
      (2, 2),
      (3, 4),
    ]
    for case in cases:
      with self.subTest(case):
        self.assertEqual(case[1], triple_step(case[0]))

if __name__ == "__main__":
  unittest.main()
