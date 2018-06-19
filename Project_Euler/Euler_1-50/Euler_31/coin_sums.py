# -*- coding: utf-8 -*-
"""In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""

def solution():
    count = 0
    for x_200 in range(0, 201, 200):
        for x_100 in range(0, 201, 100):
            for x_50 in range(0, 201, 50):
                for x_20 in range(0, 201, 20):
                    for x_10 in range(0, 201, 10):
                        for x_5 in range(0, 201, 5):
                            for x_2 in range(0, 201, 2):
                                for x_1 in range(0, 201, 1):
                                    if x_1 + x_2 + x_5 + x_10 + x_20 + x_50 + x_100 + x_200 == 200:
                                        count += 1
                                        break
    print count

solution()