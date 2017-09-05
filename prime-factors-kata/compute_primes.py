def find_factorial(num):
    prime_factors = []
    if num >= 2:
        if num % 2 == 0:
            return [2]
        if num % 3 == 0:
            return [3]
    return []
