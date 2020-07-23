from typing import List, Tuple

def solve_maze(maze: List[List[str]], r: int, c: int) -> List[Tuple[int, int]]:
  """
  Solve a maze with r rows and c columns.
  Start in upper-left and find path to lower-right.
  Can only step right or down.

  In:
  maze: Maze to solve.
  r: Number of rows in maze.
  c: Number of columns in maze.

  Out: Solution path coordinates.
  """

  coord = (0, 0)
  path, solution = [], []

  # Backtracking step
  path.append(coord)
  step(path, solution, maze, r, c)
  path.pop()

  return solution

def step(path: List[Tuple[int, int]], solution: List[Tuple[int, int]], maze: List[List[str]], r: int, c: int) -> None:
  """
  A coordinate in a maze is a step towards a solution.

  In:
  path: Current path towards a solution.
  solution: Solution of maze.
  maze: Maze to solve.
  r: Number of rows in maze.
  c: Number of columns in maze.
  """

  idx = len(path) - 1

  # Solution found
  if path[idx][0] == r - 1 and path[idx][1] == c - 1:
    solution.extend(path)
    return

  # Illegal coordinate
  if illegal(path[idx], maze, r, c):
    return

  # Step right
  path.append((path[idx][0], path[idx][1] + 1))
  step(path, solution, maze, r, c)
  path.pop()

  # Step down
  path.append((path[idx][0] + 1, path[idx][1]))
  step(path, solution, maze, r, c)
  path.pop()

def illegal(coord: Tuple[int, int], maze: List[List[str]], r: int, c: int) -> bool:
  """
  A coordinate in a maze is illegal.

  In:
  coord: A coordinate in a maze.
  maze: A maze.
  r: Number of rows in maze.
  c: Number of columns in maze.

  Out: A coordinate in a maze is illegal.
  """

  if coord[0] >= r or coord[1] >= c or maze[coord[0]][coord[1]] != "-":
    return True

  return False
