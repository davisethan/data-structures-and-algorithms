
# time: O(b)
# space: O(b)

def multiply(a, b):
  """
  Write a recursive function to multiply two numbers together
  without the * operator.
  """
  if b == 0:
    return 0
  return a + multiply(a, b - 1)
