import pytest
from compute_primes import find_factorial

def test_returns_emty_list_for_num_less_than_2():
    assert find_factorials(1) == []
