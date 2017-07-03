from fractions import Fraction as frac

"""
These execises are from w3 school on recursion
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""

"""
Exercise 1
"""
def sum_of_list(a_list):

    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] + sum_of_list(a_list[1:])

# print sum_of_list([1, 2, 3])

data_list = [1, 2, [3,4], [5,6], [1,2,3]]

"""
Exercise 3
"""
def list_sum_advanced_s(a_list_of_list):
    #Can take in a list of lists
    #base case
    if len(a_list_of_list) == 1:

        if type(a_list_of_list[0]) == int:
            return a_list_of_list[0]
        else:
            total = 0
            for x in a_list_of_list[0]:
                total += x
            return total

    else:
        if type(a_list_of_list[0]) == int:
            return a_list_of_list[0] + list_sum_advanced_s(a_list_of_list[1:])
        else:
            total = 0
            for x in a_list_of_list[0]:
                total += x

            return total + list_sum_advanced_s(a_list_of_list[1:])

# print list_sum_advanced_s(data_list)

#following is the solution from website
def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == list:
            total = total + recursive_list_sum(element)
        else:
            total = total + element
    return total

# print recursive_list_sum(data_list)
            
"""
Exercise 4
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print factorial(5)

def factorial_2(n):
    total = 1
    for x in range(1, n+1):
        total = total * x
    return total

# print factorial_2(5)

"""
Exercise 5
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(35))

"""
Exercise 6
"""
an_int = 345
"""Solution without recursion"""
def integer_sum(an_int):
    #takes an integer as an arguement
    print sum(map(int, list(str(an_int))))
    # print sum[map(int, list(str(an_int)))]

# integer_sum(an_int)

"""Solution with recursion"""
def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(int(n / 10))

# print(sumDigits(345))
# print(sumDigits(45))

"""
Exercise 7
"""
def sum_of_even(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_even(n-2)

# print sum_of_even(1997)

#Found something interesting, the maximum recursions
#allowed for sum_of_even function is 1996. With 1997
#or more, it crashes and gives the following error:
#RuntimeError: maximum recursion depth exceeded

"""
Exercise 8
"""
def harmonic_sum_s(n):
    if n == 1:
        return frac(1, 2)
    else:
        return frac(1, 2**n) + harmonic_sum_s(n - 1)

# print harmonic_sum_s(10)

"""
Exercise 9
"""
def geometric_sum(n):
    if n == 1:
        return 1
    else:
        return frac(1, n) + geometric_sum(n-1)

# print geometric_sum(4)

"""
Exercise 10
"""

def power(a, b):
    if b == 0:
        return 1

    elif a == 0:
        return 1

    elif b == 1:
        return a

    else:
        return a * power(a, b-1)

# print power(3, 4)


"""
Exercise 11
"""
def gcd(a, b):

    remainder = a % b

    if remainder == 0:
        return b
    
    else:
        return gcd(b, remainder)
    print b
        
print gcd(11, 3)


def Recurgcd(a, b):
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high

    elif low == 1:
        return 1

    else:
        return Recurgcd(low, high%low)

print(Recurgcd(12,14))











