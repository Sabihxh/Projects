# -*-coding: utf-8 -*-
"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""
from math import sqrt, floor

def solution(x):
    # x = start of range
    for i in xrange(x, x*2):
        den = i*(i-1)
        target_num = den//2
        sqrt_num = int(sqrt(target_num)) + 1
        num = sqrt_num * (sqrt_num - 1)
        if num == target_num:
            print('Total Discs: %s\nBlue Discs: %s' % (i, sqrt_num))
            return sqrt_num + 1
    print('No solution found between %s and %s' % (x, x*2))


solution(10**8)
