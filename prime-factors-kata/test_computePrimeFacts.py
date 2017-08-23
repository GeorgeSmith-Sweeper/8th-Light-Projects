import pytest
from computePrimeFacts import computePrimeFactors

def test_should_return_NONE_if_number_is_0():
		assert computePrimeFactors(0) == [];

def test_should_return_NONE_if_number_is_1():
		assert computePrimeFactors(1) == [];

'''
def test_should_return_true_if_number_is_even():
		assert isNumberEven(2) == True

def test_should_return_true_if_number_is_even():
		assert isNumberEven(3) == False

def test_if_passing_2_returns_2():
		assert primeFactorsCompute(2) == [2]

def test_if_passing_3_returns_3():
		assert primeFactorsCompute(3) == [3]
'''
