from math import sqrt
import decimal

def numbers(n):

    num = (5.236)**n
    precise = (3+sqrt(5))**n
    # getcontext().prec = 100
    # print decimal.Decimal(5).sqrt()
    # precicer = (3+(Decimal(5).sqrt()))**n

    return num, precise, precicer

print numbers(30)


