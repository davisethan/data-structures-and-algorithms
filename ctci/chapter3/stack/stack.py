
class EmptyStackException(Exception):
  pass

class StackNode:
  def __init__(self, val):
    self._val = val
    self._next = None

  @property
  def val(self):
    return self._val

  @property
  def next(self):
    return self._next

  @val.setter
  def val(self, new_val):
    self._val = new_val

  @next.setter
  def next(self, new_next):
    self._next = new_next

class Stack:
  def __init__(self):
    self._top = None

  @property
  def top(self):
    return self._top

  @top.setter
  def top(self, new_top):
    self._top = new_top

  def pop(self):
    if self.is_empty():
      raise EmptyStackException()

    old_top = self.top
    self.top = old_top.next
    return old_top.val

  def push(self, val):
    new_top = StackNode(val)
    new_top.next = self.top
    self.top = new_top

  def peek(self):
    if self.is_empty():
      raise EmptyStackException()

    return self.top.val

  def is_empty(self):
    return self.top == None
