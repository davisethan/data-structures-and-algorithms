import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):
  def test_multiply(self):
    # (multiplicand, multiplier, product)
    cases = [
      (4, 3, 12)
    ]
    for case in cases:
      with self.subTest(case):
        self.assertEqual(case[2], multiply(case[0], case[1]))

if __name__ == "__main__":
  unittest.main()
