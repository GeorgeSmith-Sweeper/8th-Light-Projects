import pytest
from prime_factors import compute_prime_factors

def test_one():
		assert compute_prime_factors(1) == []

def test_2_returns_2():
		assert compute_prime_factors(2) == [2]

def test_3_returns_3():
		assert compute_prime_factors(3) == [3]

def test_4_returns_2_2():
		assert compute_prime_factors(4) == [2, 2]

def test_6_returns_2_3():
		assert compute_prime_factors(6) == [2, 3]

def test_10_returns_2_5():
		assert compute_prime_factors(10) == [2, 5]

