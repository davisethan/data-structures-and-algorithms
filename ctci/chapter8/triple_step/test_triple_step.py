import pytest
from triple_step import triple_step

@pytest.mark.parametrize('n, expected', [
  (2, 2),
  (3, 4)
])
def test_triple_step(n, expected):
  actual = triple_step(n)
  assert actual == expected
