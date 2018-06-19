def proper_divisors(num):
    divisor_list = []
    for x in range(1,num):
        if num % x == 0:
            divisor_list.append(x)
    # print divisor_list
    return divisor_list