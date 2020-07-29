
# time: O(n2^n)
# space: O(2^n)

def power_set(aset):
  """
  Return all subsets of a set.
  """
  def power_set_step(cur, seen, aset):
    for el in aset:
      if el not in cur:
        cur.add(el)
        if cur not in seen:
          seen.add(frozenset(cur))
          power_set_step(cur, seen, aset)
        cur.remove(el)

  cur = set()
  seen = {frozenset(cur)}
  power_set_step(cur, seen, aset)
  return seen
