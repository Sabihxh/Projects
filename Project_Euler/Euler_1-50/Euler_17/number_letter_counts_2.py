#count 1 to 9
def one_to_nine():
    sums = 3+3+5+4+4+3+5+5+4
    print sums
    return sums

# one_to_nine()

#count 10 - 19
def ten_nineteen():
    sums = 3+6+6+8+8+7+7+9+8+8
    print sums
    return sums

# ten_nineteen()

#count 20 - 99
def twenty_ninetynine():
    sums = 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8 * one_to_nine()
    print sums
    return sums

# twenty_ninetynine()

def one_ninetynine():
    sums = one_to_nine() + ten_nineteen() + twenty_ninetynine() 
    print sums
    return sums

one_ninetynine()


# count 100 - 999
def hundred_nine():
    #100 to 199
    sums = (9 * one_ninetynine()) + one_to_nine() + 13 * 9
    print sums
    return sums

hundred_nine()
# def count_all():
#     sums = one_to_nine() + ten_nineteen() + twenty_ninetynine() + hundred_nine()
#     return sums

# print(count_all()) 