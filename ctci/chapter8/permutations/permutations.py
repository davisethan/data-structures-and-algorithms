
# time: O(n!)
# space: O(n!)

def permutations(chars):
  """Find all permutations of a string."""
  size = len(chars)
  perm = ""
  seen = set()
  step(chars, size, perm, seen)
  return seen

def step(chars, size, perm, seen):
  """
  Make and record permutation of a string.
  
  chars: Remaining chars in permutation.
  size: Length of finished permutation.
  perm: Current permutation.
  seen: Set of finished permutations.
  """
  # Base case
  if len(perm) == size:
    seen.add(perm)

  for idx in range(len(chars)):
    new_perm = perm + chars[idx]
    new_chars = chars[:idx] + chars[idx+1:]
    step(new_chars, size, new_perm, seen)

# Tests
# (input, expected_output)
cases = [
  ("a", {"a"}),
  ("ab", {"ab", "ba"}),
  ("abc", {"abc", "acb", "bac", "bca", "cab", "cba"}),
]
for case in cases:
  chars = case[0]

  actual = permutations(chars)
  expected = case[1]
  assert actual == expected
