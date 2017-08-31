import pytest
from compute_primes import find_factorial

def test_should_return_emty_list_with_1():
    assert find_factorial(1) == []

