
# time: O(n!)
# space: O(n!)

def parens(num):
  """Record all open and close n-pairs of parens."""
  chars = "("
  counter = {
    "(": 1,
    ")": 0
  }
  seen = set()
  step(chars, counter, num, seen)
  return seen

def step(chars, counter, size, seen):
  """
  Make and record n-pairs of parens.

  chars: Current parens.
  counter: Current number of open and close parens.
  size: n-pair size.
  seen: Finished parens.
  """
  # Illegal parens
  # 1. Too many open parens
  # 2. More close parens than open parens
  if counter["("] > size or counter["("] < counter[")"]:
    return
  # Finished parens
  if counter["("] == size and counter[")"] == size:
    seen.add(chars)
  # Unfinished parens
  # Go left, backtracking algo
  counter["("] += 1
  step(chars+"(", counter, size, seen)
  counter["("] -= 1
  # Go right, backtracking algo
  counter[")"] += 1
  step(chars+")", counter, size, seen)
  counter[")"] -= 1

# Tests
# (input, expected_output)
cases = (
  (1, {"()"}),
  (2, {"(())", "()()"}),
  (3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),
)
for case in cases:
  num = case[0]
  
  actual = parens(num)
  expected = case[1]
  assert actual == expected
