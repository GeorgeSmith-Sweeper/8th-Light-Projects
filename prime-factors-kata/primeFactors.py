def computePrimeFactors(num):
		prime_factors = []
		current_prime = 2
		while num > 1:
				if num % current_prime == 0:
						num = num / current_prime
						prime_factors.append(current_prime)
				else:
						current_prime += 1
		return prime_factors
