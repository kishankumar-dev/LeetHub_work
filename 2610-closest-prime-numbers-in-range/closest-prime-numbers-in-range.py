class Solution(object):
    def closestPrimes(self, left, right):
        def sieve(max_num):
            is_prime = [True] * (max_num + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(max_num**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, max_num + 1, i):
                        is_prime[j] = False
            return is_prime

        is_prime = sieve(right)
        primes_in_range = [i for i in range(left, right + 1) if is_prime[i]]

        if len(primes_in_range) < 2:
            return [-1, -1]

        closest_pair = [primes_in_range[0], primes_in_range[1]]
        for i in range(1, len(primes_in_range) - 1):
            if primes_in_range[i + 1] - primes_in_range[i] < closest_pair[1] - closest_pair[0]:
                closest_pair = [primes_in_range[i], primes_in_range[i + 1]]

        return closest_pair

