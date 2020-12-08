
# time: O(multiplier)
# space: O(multiplier)

def multiply(multiplicand, multiplier):
  """
  Recursivly multiply two factors without * operator.
  """
  if multiplier == 0:
    return 0
  return multiplicand + multiply(multiplicand, multiplier - 1)
