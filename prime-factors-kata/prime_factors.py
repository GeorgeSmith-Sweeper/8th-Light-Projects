def compute_prime_factors(num):
		current_prime = 2
		prime_factors = []
		while num >= current_prime:
				if num % current_prime == 0:
						prime_factors.append(current_prime)
						num /= 2
				else:
						current_prime += 1
		return prime_factors
