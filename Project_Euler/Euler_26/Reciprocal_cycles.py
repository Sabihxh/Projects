from decimal import *
getcontext().prec = 1000
Decimal(2).sqrt()



for x in range(1, 1000):
    value = Decimal(1)/Decimal(x)
    print value