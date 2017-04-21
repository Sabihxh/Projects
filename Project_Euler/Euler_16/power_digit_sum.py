#power_of_two calculates 2^x
def power_of_two(power):
    product = 1
    for x in range(power):
        product *= 2
    # print product
    return product

#add_nums adds all digits of a number
def add_nums(power):
    sums = 0
    string = str(power_of_two(power))
    for x in string:
        sums += int(x)
    print sums
    return sums

add_nums(1000)