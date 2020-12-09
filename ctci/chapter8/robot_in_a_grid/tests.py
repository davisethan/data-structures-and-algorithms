import unittest
from robot_in_a_grid import solve_maze

class TestSolveMaze(unittest.TestCase):
  def test_solve_maze(self):
    # (maze, rows, columns, maze_solution)
    cases = [
      (
        [
          ['-', '-', '+'],
          ['+', '-', '+'],
          ['+', '-', '+'],
          ['+', '-', '-']
        ],
        4,
        3,
        [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]
      ),
      (
        [
          ['-', '-', '-'],
          ['+', '-', '+'],
          ['+', '-', '+'],
          ['+', '-', '-']
        ],
        4,
        3,
        [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]
      )
    ]
    for index, case in enumerate(cases):
      with self.subTest(index):
        self.assertEqual(case[3], solve_maze(case[0], case[1], case[2]))

if __name__ == "__main__":
  unittest.main()
