import unittest
from stack import Stack, EmptyStackException

class TestStackPush(unittest.TestCase):
  def test_empty_stack_push(self):
    stack = Stack()
    stack_data = 0
    stack.push(stack_data)
    self.assertEqual(stack_data, stack.get_top().get_data())

  def test_nonempty_stack_push(self):
    stack = Stack()
    stack_data = (0, 1)
    for data in stack_data:
      stack.push(data)
    self.assertEqual(stack_data[1], stack.get_top().get_data())
    self.assertEqual(stack_data[0], stack.get_top().get_next().get_data())
    self.assertEqual(None, stack.get_top().get_next().get_next())

class TestStackPeek(unittest.TestCase):
  def test_peek_empty_stack_top(self):
    stack = Stack()
    with self.assertRaises(EmptyStackException):
      stack.peek()

  def test_peek_nonempty_stack_top(self):
    stack = Stack()
    stack_data = 0
    stack.push(stack_data)
    self.assertEqual(stack_data, stack.peek())

class TestStackIsEmpty(unittest.TestCase):
  def test_stack_is_empty(self):
    stack = Stack()
    self.assertTrue(stack.is_empty())

  def test_stack_not_empty(self):
    stack = Stack()
    stack_data = 0
    stack.push(stack_data)
    self.assertFalse(stack.is_empty())

class TestStackPop(unittest.TestCase):
  def test_pop_empty_stack(self):
    stack = Stack()
    with self.assertRaises(EmptyStackException):
      stack.pop()

  def test_pop_single_node_stack(self):
    stack = Stack()
    stack_data = 0
    stack.push(stack_data)
    node = stack.pop()
    self.assertEqual(stack_data, node.get_data())
    self.assertEqual(None, stack.get_top())

  def test_pop_double_node_stack(self):
    stack = Stack()
    stack_data = (0, 1)
    for data in stack_data:
      stack.push(data)
    node = stack.pop()
    self.assertEqual(stack_data[1], node.get_data())
    self.assertEqual(stack_data[0], stack.get_top().get_data())
    self.assertEqual(None, stack.get_top().get_next())

if __name__ == "__main__":
  unittest.main()
