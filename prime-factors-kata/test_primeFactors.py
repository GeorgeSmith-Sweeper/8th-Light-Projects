import pytest
from primeFactors import computePrimeFactors

def test_returns_empty_list_with_input_1():
		assert computePrimeFactors(1) == []

def test_returns_2_list_with_input_2():
		assert computePrimeFactors(2) == [2]

def test_returns_3_list_with_input_3():
		assert computePrimeFactors(3) == [3]

def test_returns_2_2_list_with_input_4():
		assert computePrimeFactors(4) == [2,2]

def test_returns_2_2_2_list_with_input_8():
		assert computePrimeFactors(8) == [2,2,2]

def test_returns_3_3_list_with_input_9():
		assert computePrimeFactors(9) == [3,3]

def test_returns_2_7_7_list_with_input_98():
		assert computePrimeFactors(98) == [2,7,7]

