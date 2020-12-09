from typing import List, Tuple

def solve_maze(
  maze: List[List[str]],
  rows: int,
  columns: int) -> List[Tuple[int, int]]:
  """
  Solve a maze.
  Start in upper-left and find path to lower-right.
  Can only step right or down.

  In:
  maze: Maze to solve.
  rows: Number of rows in maze.
  columns: Number of columns in maze.

  Out: Solution path coordinates.
  """
  starting_coordinates = (0, 0)
  current_path = []
  solution_path = []

  # Backtracking step
  current_path.append(starting_coordinates)
  solve_maze_step(current_path, solution_path, maze, rows, columns)
  current_path.pop()

  return solution_path

def solve_maze_step(
  current_path: List[Tuple[int, int]],
  solution_path: List[Tuple[int, int]],
  maze: List[List[str]],
  rows: int,
  columns: int) -> None:
  """
  A coordinate in a maze is a step towards a solution.

  In:
  path: Current path towards a solution.
  solution: Solution path of maze.
  maze: Maze to solve.
  r: Number of rows in maze.
  c: Number of columns in maze.
  """
  current_path_last_index = len(current_path) - 1
  maze_coordinates = current_path[current_path_last_index]

  # Solution found
  if maze_coordinates[0] == rows - 1 and maze_coordinates[1] == columns - 1:
    solution_path.extend(current_path)
    return

  # Illegal coordinate
  if is_illegal(maze_coordinates, maze, rows, columns):
    return

  # Step right
  current_path.append((maze_coordinates[0], maze_coordinates[1] + 1))
  solve_maze_step(current_path, solution_path, maze, rows, columns)
  current_path.pop()

  # Step down
  current_path.append((maze_coordinates[0] + 1, maze_coordinates[1]))
  solve_maze_step(current_path, solution_path, maze, rows, columns)
  current_path.pop()

def is_illegal(
  coordinates: Tuple[int, int],
  maze: List[List[str]],
  rows: int,
  columns: int) -> bool:
  """
  A coordinate in a maze is illegal.

  In:
  coordinates: A coordinate in a maze.
  maze: A maze.
  rows: Number of rows in maze.
  columns: Number of columns in maze.

  Out: A coordinate in a maze is illegal.
  """
  if coordinates[0] >= rows:
    return True
  elif coordinates[1] >= columns:
    return True
  elif maze[coordinates[0]][coordinates[1]] != "-":
    return True
  else:
    return False
