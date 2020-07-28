import pytest
from magic_index import magic_index

@pytest.mark.parametrize('lst, expected', [
  ([0, 2, 3, 4, 5], 0),
  ([-2, 1, 3, 4, 5], 1),
  ([-2, -1, 0, 1, 4], 4),
  ([-2, -1, 0, 3, 6], 3),
  ([2, 3, 4, 5, 6], -1),
  ([-2, -1, 0, 1, 2], -1)
])
def test_magic_index(lst, expected):
  actual = magic_index(lst)
  assert actual == expected
