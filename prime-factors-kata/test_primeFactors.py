import pytest
from prime_factors import compute_prime_factors

def test_should_return_empty_list_with_less_than_2():
		assert compute_prime_factors(0) == []

def test_should_return_2_list_with_2():
		assert compute_prime_factors(2) == [2]

def test_should_return_3_list_with_3():
		assert compute_prime_factors(3) == [3]

def test_should_return_2_2_list_with_4():
		assert compute_prime_factors(4) == [2,2]

def test_should_return_2_3_list_with_6():
		assert compute_prime_factors(6) == [2,3]

def test_should_return_2_2_list_with_8():
		assert compute_prime_factors(8) == [2,2,2]

def test_should_return_3_7_list_with_21():
		assert compute_prime_factors(21) == [3,7]

def test_should_return_2_7_7_list_with_98():
		assert compute_prime_factors(98) == [2,7,7]

