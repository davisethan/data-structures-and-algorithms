import pytest
from power_set import power_set

@pytest.mark.parametrize('aset, expected', [
  (set(), (set(),)),
  ({1}, (set(), {1},)),
  ({1, 2}, (set(), {1}, {2}, {1, 2},)),
  ({1, 2, 3}, (set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3},))
])
def test_power_set(aset, expected):
  expected = {frozenset(s) for s in expected}

  actual = power_set(aset)
  assert actual == expected
