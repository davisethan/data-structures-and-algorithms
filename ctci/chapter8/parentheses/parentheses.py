
# time: O(n!)
# space: O(n!)

def parentheses(size):
  """Record all open and close n-pairs of parenthesis."""
  characters = "("
  counter = {
    "(": 1,
    ")": 0
  }
  seen = set()
  parentheses_step(characters, counter, size, seen)
  return seen

def parentheses_step(characters, counter, size, seen):
  """
  Make and record n-pairs of parentheses.

  characters: Current parentheses.
  counter: Current number of open and close parentheses.
  size: n-pair size.
  seen: Finished parentheses.
  """
  # Illegal parentheses
  # 1. Too many open parentheses
  # 2. More close parentheses than open parentheses
  if counter["("] > size or counter["("] < counter[")"]:
    return

  # Finished parentheses
  if counter["("] == size and counter[")"] == size:
    seen.add(characters)

  # Unfinished parens
  # Go left, backtracking algo
  counter["("] += 1
  parentheses_step(characters + "(", counter, size, seen)
  counter["("] -= 1

  # Go right, backtracking algo
  counter[")"] += 1
  parentheses_step(characters + ")", counter, size, seen)
  counter[")"] -= 1
