# -*- coding: utf-8 -*-
"""
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


""" Solution
1. Get all triplets whose sum add up to integers <= 1000
e.g. smallest 

2. 
"""

def pythagoras_triplets(limit):
    triples_sum = []
    for x in range(1, limit):
        for y in range(1, limit):
            z = ((x**2) + (y**2)) ** (0.5)
            if z ** 2 == int(z) ** 2:
                sum_of_triplets = x+y+int(z)
                if sum_of_triplets <= 1000:
                    triples_sum.append(sum_of_triplets)

    a_dict = {}
    for num in triples_sum:
        if num not in a_dict:
            a_dict[num] = 1
        else:
            a_dict[num] += 1
    
    max_num = []
    for key, value in a_dict.items():
        max_num.append(value)

    for key, value in a_dict.items():
        if value == max(max_num):
            return key

print pythagoras_triplets(1000)
