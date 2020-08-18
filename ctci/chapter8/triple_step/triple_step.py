
# time: O(n)
# space: O(n)

def triple_step(n):
  """
  A child is running up a staircase of n steps with 1, 2, or 3 steps at a time.
  Find how many ways the child can reach the nth step.
  """
  def triple_step_recur(n, seen):
    if n < 0:
      return 0
    elif n == 0:
      return 1
    else:
      if n in seen:
        return seen[n]
      else:
        seen[n] = triple_step_recur(n - 3, seen) + triple_step_recur(n - 2, seen) + triple_step_recur(n - 1, seen)
        return seen[n]

  seen = {}
  return triple_step_recur(n, seen)
