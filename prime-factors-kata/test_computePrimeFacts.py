import pytest
from primeCompute import computePrimeFactors

def test_should_return_empty_list_if_number_is_0():
		assert computePrimeFactors(0) == []

def test_should_return_empty_list_if_number_is_1():
		assert computePrimeFactors(1) == []

def test_should_return_list_with_2_if_number_is_2():
		assert computePrimeFactors(2) == [2]

def test_should_return_list_with_3_if_number_is_3():
		assert computePrimeFactors(3) == [3]

def test_should_return_list_with_2_2_if_number_is_4():
		assert computePrimeFactors(4) == [2,2]

def test_should_return_list_with_5_if_number_is_5():
		assert computePrimeFactors(5) == [5]

def test_should_return_list_with_2_3_if_number_is_6():
		assert computePrimeFactors(6) == [2,3]

