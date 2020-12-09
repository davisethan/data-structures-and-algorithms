
def towers_of_hanoi(towers):
  """Solve towers of hanoi."""
  origin_tower = 0
  neighbor_tower = 1
  destination_tower = 2
  tower_index = 0

  move_disks(towers, origin_tower, tower_index, destination_tower, neighbor_tower)

def move_disks(towers, origin_tower, tower_index, destination_tower, neighbor_tower):
  """Move towers of hanoi disk."""
  # Move upper disks away
  disks = towers[origin_tower][tower_index + 1:]
  if disks:
    move_disks(towers, origin_tower, tower_index + 1, neighbor_tower, destination_tower)
  
  # Move lower disk
  towers[destination_tower].append(towers[origin_tower].pop())

  # Move upper disks back on lower disk
  if towers[destination_tower][-1] - 1 in towers[neighbor_tower]:
    neighbor_index = towers[neighbor_tower].index(towers[destination_tower][-1] - 1)
    disks = towers[neighbor_tower][neighbor_index:]
    if disks:
      move_disks(towers, neighbor_tower, neighbor_index, destination_tower, origin_tower)
