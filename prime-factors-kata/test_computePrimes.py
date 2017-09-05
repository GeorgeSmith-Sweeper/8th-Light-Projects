import pytest
from compute_primes import find_factorial

def test_find_factorial_returns_emp_list_with_1():
    assert find_factorial(1) == []

def test_find_factorial_returns_2_list_with_2():
    assert find_factorial(2) == [2]

def test_find_factorial_returns_3_list_with_3():
    assert find_factorial(3) == [3]

def test_find_factorial_returns_2_2_list_with_4():
    assert find_factorial(4) == [2, 2]


