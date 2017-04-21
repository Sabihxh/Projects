import math

#Returns True if string is palindrome
def is_palindrome(string):
    string = str(string)

    if string == ''.join(list(string)[::-1]):
        return True
    else:
        return False

#returns a set of all numbers that are palindromes up to the limit
def _palin_num_generator(limit):
    palin_set = set()
    for num in range(1, limit + 1):
        if is_palindrome(num):
            palin_set.add(num)
            print num

#Sums all numbers that are palindromic in base 10 and base 2
def _doublebase_palins(limit):
    palin_set = set()
    for num in range(1, limit + 1):
        if is_palindrome(num) and is_palindrome(bin(num)[2:]):
            palin_set.add(num)
            print num, bin(num)[2:]
    print sum(palin_set)
    return sum(palin_set)


_doublebase_palins(1000000)











# def int_to_binary(x):
#     limit = int(math.log(x, 2)) + 1
#     binary = ''
#     for num in range(limit):
#         if x % 2 == 0:
#             binary += '0'
#             x = x/2
#             print x
#         else:
#             binary += '1'
#             x = int(x/2) + 1


#     return binary


# print int_to_binary(32)

# for x in range(1, 1000):
#     if str(x) == str(x)[::-1]:
#         pass
