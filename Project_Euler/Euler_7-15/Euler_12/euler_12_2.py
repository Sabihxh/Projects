import math #for square root
from itertools import groupby

#Takes a number and returns the number of factors it has
def _factors_counter(num):
    factors = 2 #Since 1 and n are always factors so there are already 2 factors
    limit = int(math.sqrt(num))
    for i in range(2, limit + 1): #Only need to check for factors upto square root of num
        if num % i == 0: #if number is divisible by a number then we add 2 to factors
            factors += 2
    return factors

#Enter num value to output the num-th trianglar number
def triangular_numbers(num):
    tri_num = 1
    for x in range(2, num + 1): #adds all the numbers from 1 to num e.g. if num = 3 then 1+2+3 = 6
        tri_num += x
    return tri_num

#This loops until it finds a triangluar number whose factors are equal to the input (num). 
def answer(num):
    i = 1
    while _factors_counter(triangular_numbers(i)) <= factors:
        i += 1
    print('Triangular number: %d' % triangular_numbers(i))
    print('Number of factors: %d' % _factors_counter(triangular_numbers(i)))

answer(500)


