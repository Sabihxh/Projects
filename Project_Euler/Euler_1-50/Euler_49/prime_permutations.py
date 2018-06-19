from itertools import permutations

#is_prime function taken from https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
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

def solution():
    ultimate_list = []
    for x_1 in range(1001, 1005):
        x_2 = x_1 + 3330
        x_3 = x_2 + 6660
        for row in permutations()
        # if is_prime(x_1) and is_prime(x_2) and is_prime(x_3):
            # print 

        

solution()