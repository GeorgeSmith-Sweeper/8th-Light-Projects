import pytest
from prime_factors import compute_prime_factors

def test_returns_empty_list_when_value_is_1():
		assert compute_prime_factors(1) == []

def test_returns_2_list_when_value_is_2():
		assert compute_prime_factors(2) == [2]

def test_returns_3_list_when_value_is_3():
		assert compute_prime_factors(3) == [3]

def test_returns_2_2_list_when_value_is_4():
		assert compute_prime_factors(4) == [2,2]

def test_returns_2_3_list_when_value_is_6():
		assert compute_prime_factors(6) == [2,3]

