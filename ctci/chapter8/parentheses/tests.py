import unittest
from parentheses import parentheses

class TestParentheses(unittest.TestCase):
    def test_parentheses(self):
        # (Number of open/close parentheses, All open/close parentheses permuations)
        cases = [
            (1, {"()"}),
            (2, {"(())", "()()"}),
            (3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),
        ]
        for case in cases:
            self.assertEqual(case[1], parentheses(case[0]))

if __name__ == "__main__":
    unittest.main()
