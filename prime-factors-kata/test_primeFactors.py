import pytest
from prime_factors import compute_prime_factors

def test_returns_2_list_with_input_2():
		assert compute_prime_factors(2) == [2]

def test_returns_3_list_with_input_3():
		assert compute_prime_factors(3) == [3]

def test_returns_2_2_list_with_input_4():
		assert compute_prime_factors(4) == [2,2]

def test_returns_2_3_list_with_input_6():
		assert compute_prime_factors(6) == [2,3]

def test_returns_3_3_list_with_input_9():
		assert compute_prime_factors(9) == [3,3]

def test_returns_3_7_list_with_input_21():
		assert compute_prime_factors(21) == [3,7]

def test_returns_2_7_7_list_with_input_98():
		assert compute_prime_factors(98) == [2,7,7]

