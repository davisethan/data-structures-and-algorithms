
# time: O(n2^n)
# space: O(2^n)

def power_set(lot):
  """
  Return all subsets of a set.
  """
  current_set = set()
  seen = {frozenset(current_set)}
  power_set_step(current_set, seen, lot)
  return seen

def power_set_step(current_set, seen, lot):
  for element in lot:
    if element not in current_set:
      current_set.add(element)
      if current_set not in seen:
        seen.add(frozenset(current_set))
        power_set_step(current_set, seen, lot)
      current_set.remove(element)
