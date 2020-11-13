
def towers_of_hanoi(towers):
  """Solve towers of hanoi."""
  orig = 0
  nbr = 1
  dest = 2
  idx = 0

  move(towers, orig, idx, dest, nbr)


def move(towers, orig, idx, dest, nbr):
  """Move towers of hanoi disk."""
  # Move upper disks away
  disks = towers[orig][idx+1:]
  if disks:
    move(towers, orig, idx+1, nbr, dest)
  
  # Move lower disk
  towers[dest].append(towers[orig].pop())

  # Move upper disks back on lower disk
  if towers[dest][-1]-1 in towers[nbr]:
    nbr_idx = towers[nbr].index(towers[dest][-1]-1)
    disks = towers[nbr][nbr_idx:]
    if disks:
      move(towers, nbr, nbr_idx, dest, orig)


# Tests
# (input, expected_output)
cases = [
  (([1], [], []), ([], [], [1])),
  (([2, 1], [], []), ([], [], [2, 1])),
  (([3, 2, 1], [], []), ([], [], [3, 2, 1])),
  (([4, 3, 2, 1], [], []), ([], [], [4, 3, 2, 1])),
  (([5, 4, 3, 2, 1], [], []), ([], [], [5, 4, 3, 2, 1])),
]
for case in cases:
  towers = case[0]
  towers_of_hanoi(towers)
  
  actual = towers
  expected = case[1]
  assert actual == expected
