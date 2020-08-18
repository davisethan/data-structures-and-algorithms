import pytest
from multiply import multiply

@pytest.mark.parametrize('a, b, expected', [
  (4, 3, 12)
])
def test_multiply(a, b, expected):
  actual = multiply(a, b)
  assert actual == expected
