#-*- coding: utf-8 -*-
import itertools

"""Prime digit replacements
By replacing the 1st digit of the 2-digit number *3, it turns out 
that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
ß with the same digit, is part of an eight prime value family."""


def is_prime(n):
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


def combinations_generator(_num):
    """Takes _num as input and outputs all 
    the combinations nCr for r = 1, 2, ... , n-1
    e.g. 
    Input _num = 3,
    Output: [(1), (2), (3), (1, 2), (1, 3), (2, 3)]
    """
    looper = range(1, _num)
    result = []
    for L in looper:
        for subset in itertools.combinations(range(1, _num + 1), L):
            result.append(subset)
    print result
    return result

combinations_generator(4)

def solution():
    max_no_of_primes, max_primes_chain = 0, []
    combinations = combinations_generator(3)
    print combinations
    a_string = '0000'
    for x in range(1, 9):
        for combi in combinations:
            for a_num in combi:

    #     if is_prime(x):
    #         no_of_primes += 1
    #         temp_chain.append(x)

    #     if no_of_primes > max_no_of_primes:
    #         max_no_of_primes = no_of_primes
    #         max_primes_chain = temp_chain

    # print max_no_of_primes, max_primes_chain

solution()

# def n_combinations(_num):














