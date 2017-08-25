import pytest
from primeFactors import computePrimeFactors

def test_returns_empty_list_with_input_1():
		assert computePrimeFactors(1) == []

def test_returns_2_list_with_input_2():
		assert computePrimeFactors(2) == [2]

def test_returns_3_list_with_input_3():
		assert computePrimeFactors(3) == [3]

