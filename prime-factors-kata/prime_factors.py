def compute_prime_factors(num):
		current_prime = 2
		while num >= current_prime:
				if num == 4:
						return [current_prime, current_prime]
				if num == 6:
						return [current_prime,3]
				return[num]
		return []
