import pytest
from stack import Stack, EmptyStackException

@pytest.fixture
def stack():
  return Stack()

def test_zero_node_stack(stack):
  assert stack.is_empty() == True

  with pytest.raises(EmptyStackException):
    stack.peek()

  with pytest.raises(EmptyStackException):
    stack.pop()

  val = 0
  stack.push(val)

def test_one_node_stack(stack):
  val = 0
  stack.push(val)
  assert stack.is_empty() == False
  assert stack.peek() == val
  assert stack.pop() == val
  assert stack.is_empty() == True

def test_two_node_stack(stack):
  vals = [0, 1]
  stack.push(vals[0])
  stack.push(vals[1])
  assert stack.pop() == vals[1]
  assert stack.is_empty() == False
