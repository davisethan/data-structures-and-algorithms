
def magic_index(lst):
  """
  A magic index in a list L[0...n-1] is where L[i] = i.
  Find a magic index in a list of sorted distinct integers.
  """
  def magic_index_step(lst, idx):
    if len(lst) == 0:
      return -1

    mid = len(lst) // 2
    if lst[mid] < idx:
      new_lst = lst[mid + 1:]
      new_idx = idx + len(new_lst) // 2 + 1
      return magic_index_step(new_lst, new_idx)
    elif lst[mid] > idx:
      new_lst = lst[:mid]
      new_idx = idx - (len(new_lst) + 1) // 2
      return magic_index_step(new_lst, new_idx)
    else:
      return idx

  idx = len(lst) // 2
  return magic_index_step(lst, idx)
