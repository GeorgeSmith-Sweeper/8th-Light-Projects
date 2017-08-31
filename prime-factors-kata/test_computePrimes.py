import pytest
from compute_primes import find_factorial

def test_should_return_emty_list_with_1():
    assert find_factorial(1) == []

def test_should_return_2_list_with_2():
    assert find_factorial(2) == [2]

def test_should_return_3_list_with_3():
    assert find_factorial(3) == [3]

def test_should_2_2_list_with_4():
    assert find_factorial(4) == [2, 2]
    
def test_should_return_2_3_with_6():
    assert find_factorial(6) == [2, 3]

def test_should_return_2_5_with_10():
    assert find_factorial(10) == [2, 5]
    
def test_should_2_7_with_21():
    assert find_factorial(21) == [3, 7]

def test_should_2_7_7_with_98():
    assert find_factorial(98) == [2, 7, 7]
