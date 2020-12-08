
def magic_index(integers):
  """
  A magic index in a list L[0...n-1] is where L[i] = i.
  Find a magic index in a list of sorted distinct integers.
  """
  middle_index = len(integers) // 2
  return magic_index_step(integers, middle_index)

def magic_index_step(integers, index):
    if 0 == len(integers):
      return -1

    middle_index = len(integers) // 2
    if integers[middle_index] < index:
      new_integers = integers[middle_index + 1:]
      new_index = index + len(new_integers) // 2 + 1
      return magic_index_step(new_integers, new_index)
    elif integers[middle_index] > index:
      new_integers = integers[:middle_index]
      new_index = index - (len(new_integers) + 1) // 2
      return magic_index_step(new_integers, new_index)
    else:
      return index
