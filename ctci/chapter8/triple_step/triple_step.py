
# time: O(steps)
# space: O(steps)

def triple_step(steps):
  """
  A child is running up a staircase of N steps with 1, 2, or 3 steps at a time.
  Find how many ways the child can reach the Nth step.
  """
  seen = {}
  return triple_step_recursion(steps, seen)

def triple_step_recursion(steps, seen):
    if steps < 0:
      return 0
    elif steps == 0:
      return 1
    else:
      if steps in seen:
        return seen[steps]
      else:
        seen[steps] = triple_step_recursion(steps - 3, seen)
        seen[steps] += triple_step_recursion(steps - 2, seen)
        seen[steps] += triple_step_recursion(steps - 1, seen)
        return seen[steps]
