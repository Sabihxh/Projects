import math #for square root
from itertools import groupby

#enter num value to output the num-th trianglar number
def _triangular_numbers(num):
    tri_num = 1
    for x in range(2, num + 1):
        tri_num += x
    return tri_num


#This function checks whether a number is prime or not
def prime_checker(prime):
    limit = int(math.sqrt(prime))
    for x in range(2, limit + 1):
        if prime % x == 0:
            return False
    return True

#This function finds all prime factors of integer and put it in a list
def _prime_factors(integer):
    list_of_primes = []
    limit = (integer)/2
    for x in range(2, limit + 3):
        if integer % x == 0 and prime_checker(x):
            while integer % x == 0:
                list_of_primes.append(x)
                integer = integer/x
    return list_of_primes


#This function counts the frequency of each element in a list
#e.g. input: [1,1,1,4,4,5,5,5] and output: [3,2,3]
#Assumption: Input is a sorted list
def _number_of_duplicates(alist):
    return [len(list(group)) for key, group in groupby(alist)]

#Adds 1 to each element in a list and multiplies them all together
def _multiply_list_elements(alist):
    product = 1
    for x in alist:
        x += 1
        product *= x
    return product

def tri_num_with_9_factors():

    tri_num = 1
    while _multiply_list_elements(_number_of_duplicates(_prime_factors(_triangular_numbers(tri_num)))) <= 500:
        result = _triangular_numbers(tri_num)
        tri_num += 1

    print('Triangular number: %d' % _triangular_numbers(tri_num))
    print('Number of Factors: %d' % _multiply_list_elements(_number_of_duplicates(_prime_factors(_triangular_numbers(tri_num)))))

    return _triangular_numbers(tri_num)

tri_num_with_9_factors()
    























