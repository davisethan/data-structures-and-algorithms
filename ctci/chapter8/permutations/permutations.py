
# time: O(n!)
# space: O(n!)

def permutations(characters):
  """Find all permutations of a string."""
  size = len(characters)
  permutation = ""
  seen = set()
  permutations_step(characters, size, permutation, seen)
  return seen

def permutations_step(characters, size, permutation, seen):
  """
  Make and record permutation of a string.
  
  characters: Remaining characters in permutation.
  size: Length of finished permutation.
  permutation: Current permutation.
  seen: Set of finished permutations.
  """
  # Base case
  if len(permutation) == size:
    seen.add(permutation)

  for index in range(len(characters)):
    new_permutation = permutation + characters[index]
    new_characters = characters[:index] + characters[index + 1:]
    permutations_step(new_characters, size, new_permutation, seen)
