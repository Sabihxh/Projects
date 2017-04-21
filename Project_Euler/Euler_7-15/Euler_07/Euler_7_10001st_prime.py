# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math

#Checks if a number is prime, if prime then returns True, otherwise returns False
def prime_checker(prime):
    limit = int(math.sqrt(prime))
    for x in range(2, limit + 1):
        if prime % x == 0:
            return False
    return True

def prime_counting():
    prime_list = [1]
    counter = 0
    for x in range(2,104758):
        if prime_checker(x):
            counter += 1
            prime_list.append(x)
            prime_list.pop(0)
    print(prime_list)
    print(counter)

#prime_counting()

def prime_counting_2():
    x = 1
    y = 3
    while x < 10001:
        if prime_checker(y):
            x += 1
        y += 1
    print(y-1)
prime_counting_2()



# def prime_counting_2():
#     prime_list = [1]
#     counter = 0
#     while y < 10002:
#         for x in range(2,100):
#             if prime_checker(x):
#                 counter += 1
#                 prime_list.append(x)
#                 prime_list.pop(0)
#     print(prime_list)


# def n_th_prime():
#     prime = 3
#     count = 1
#     while count < 7:
#         print(count)
#         if prime_checker(prime) == prime:
#             count += 1
#             print(count)
# n_th_prime()

