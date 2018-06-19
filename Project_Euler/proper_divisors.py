
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

def proper_divisors(num):
    """Slower than all_divisors"""
    divisor_list = []
    for x in range(1,num):
        if num % x == 0:
            divisor_list.append(x)
    # print divisor_list
    return divisor_list




def all_divisors(num):
    """Gives all divisors including num itself"""
    divisors = []
    for x in range(1, int(num**0.5) + 1):
        if num % x == 0:
            y = int(num/x)
            divisors.extend([x, y])
    # print divisor_list
    return divisors



def prime_divisors(num):
    prime_divisors = set()
    for x in range(1, int(num**0.5) + 1):
        if num % x == 0 and is_prime(x):
            prime_divisors.add(x)
    return prime_divisors


# print proper_divisors(123456789)
# print all_divisors(123456789123123)
# print prime_divisors(123456789123123)













