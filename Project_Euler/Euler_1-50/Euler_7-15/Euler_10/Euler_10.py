a = """ The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
import math

def prime_checker(prime):
    limit = int(math.sqrt(prime))
    for x in range(2, limit + 1):
        if prime % x == 0:
            return False
    return True

def prime_sum(primes_below):
    sum = 0
    for x in range(2, primes_below):
        if prime_checker(x):
            sum = sum + x
    print(sum)

prime_sum(2000000)

