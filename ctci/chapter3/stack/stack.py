
class Stack:
  def __init__(self):
    self._top = None

  def get_top(self):
    return self._top

  def push(self, data):
    node = StackNode(data)
    node.set_next(self._top)
    self._top = node

  def is_empty(self):
    return None == self._top

  def pop(self):
    if self.is_empty():
      raise EmptyStackException()
    node = self._top
    self._top = node.get_next()
    node.set_next(None)
    return node

  def peek(self):
    if self.is_empty():
      raise EmptyStackException()
    top_data = self._top.get_data()
    return top_data

class StackNode:
  def __init__(self, data):
    self._data = data
    self._next = None

  def get_data(self):
    return self._data

  def get_next(self):
    return self._next

  def set_next(self, stack_node):
    self._next = stack_node

class EmptyStackException(Exception):
  pass
