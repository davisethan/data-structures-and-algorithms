import pytest
from ctci.chapter8.robot_in_a_grid.robot_in_a_grid import solve_maze

@pytest.mark.parametrize('maze, r, c, expected', [
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
])
def test_solve_maze(maze, r, c, expected):
  actual = solve_maze(maze, r, c)
  assert actual == expected
