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

def test_should_return_list_with_7_if_number_is_7():
		assert computePrimeFactors(7) == [7]

def test_should_return_list_with_2_2_2_if_number_is_8():
		assert computePrimeFactors(8) == [2,2,2]

def test_should_return_list_with_3_3_if_number_is_9():
		assert computePrimeFactors(9) == [3,3]

def test_should_return_list_with_2_5_if_number_is_10():
		assert computePrimeFactors(10) == [2,5]

def test_should_return_list_with_11_if_number_is_11():
		assert computePrimeFactors(11) == [11]

def test_should_return_list_with_2_2_3_if_number_is_12():
		assert computePrimeFactors(12) == [2,2,3]

def test_should_return_list_with_13_if_number_is_13():
		assert computePrimeFactors(13) == [13]

def test_should_return_list_with_2_7_if_number_is_14():
		assert computePrimeFactors(14) == [2,7]

def test_should_return_list_with_3_5_if_number_is_15():
		assert computePrimeFactors(15) == [3,5]

def test_should_return_list_with_2_2_2_2_if_number_is_16():
		assert computePrimeFactors(16) == [2,2,2,2]

def test_should_return_list_with_17_if_number_is_17():
		assert computePrimeFactors(17) == [17]

def test_should_return_list_with_2_3_3_if_number_is_18():
		assert computePrimeFactors(18) == [2,3,3]

def test_should_return_list_with_19_if_number_is_19():
		assert computePrimeFactors(19) == [19]

