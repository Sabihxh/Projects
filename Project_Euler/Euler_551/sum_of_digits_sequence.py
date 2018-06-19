#-*- coding: utf-8 -*-

import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt


def mt_help():
    print help(matplotlib)

def mt_dir():
    print dir(matplotlib)


def sum_of_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

def solution():
    _ = 1
    _sum = 1
    while _ <= 100: #1000000000000000
        _sum = _sum + sum_of_digits(_sum)
        _ += 1
        print _sum,
    


