num = 220

def proper_divisors(num):
    divisor_list = []
    for x in range(1,num):
        if num % x == 0:
            divisor_list.append(x)
    # print divisor_list
    return divisor_list



def check_if_emicable(num):
    #add all the proper divisors of number
    a = sum(proper_divisors(num)) 
    b = sum(proper_divisors(a))
    # print num, a, b, '\n', '*'*10
    if b == num:
        return b

def all_amicable_nums(_limit):
    amicable_list = []
    for x in range(1, _limit + 1):
        amicable = check_if_emicable(x)
        if amicable:
            print '%s: %s' % (amicable, proper_divisors(x))
            amicable_list.append(amicable)
    return sum(amicable_list)

print all_amicable_nums(10000)