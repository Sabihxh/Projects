"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any 
order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum 
of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

def is_prime(n):
    """Return True if arguement-n is prime, otherwise False"""
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True   

def primes(prime_limit = 1000):
    """Returns a set of primes < 1000 (if no arguement is passed)"""
    primes_set = set()
    for x in range(prime_limit):
        if is_prime(x):
            primes_set.add(x)
    return primes_set

def solution():
    """Returns the first set of 5 primes in which any two primes concatenate to produce another prime """
    primes_set = primes(prime_limit = 10000)
    completed_set = set()

    for x in primes_set:
        if x in completed_set: continue
        prime_pair_sets = {x}

        for y in primes_set:
            if all([is_prime(int(str(num) + str(y))) and is_prime(int(str(y) + str(num))) for num in prime_pair_sets]):
                prime_pair_sets.add(y)
                completed_set.add(y)

        if len(prime_pair_sets) >= 5:
            print prime_pair_sets, sum(prime_pair_sets)
            return prime_pair_sets, sum(prime_pair_sets)

solution()

