import pytest
from compute_primes import find_factorial

def test_return_empty_list_with_num_1():
    assert find_factorial(1) == []

def test_return_2_list_with_num_2():
    assert find_factorial(2) == [2]

def test_return_3_list_with_num_3():
    assert find_factorial(3) == [3]

def test_return_2_2_list_with_num_4():
    assert find_factorial(4) == [2, 2]

def test_return_2_2_2_list_with_num_8():
    assert find_factorial(8) == [2, 2, 2]

def test_return_3_7_list_with_num_21():
    assert find_factorial(21) == [3, 7]

def test_return_2_7_7_with_num_98():
    assert find_factorial(98) == [2, 7, 7]

