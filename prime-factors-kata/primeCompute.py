import math

def computePrimeFactors(num, prime_factors=None):
		if prime_factors is None:
			prime_factors = []
		if num > 1:
			if num % 2 == 0:
					prime_factors.append(2)
					num = num / 2
					computePrimeFactors(num, prime_factors)
			elif num % 3 == 0:
					prime_factors.append(3)
					num = num / 3
					computePrimeFactors(num, prime_factors)
			elif num % 5 == 0:
					prime_factors.append(5)
					num = num / 5
					computePrimeFactors(num, prime_factors)
			else:
					prime_factors.append(num)
		return prime_factors
