
def prime(a_prime):
    limit = int(a_prime/2 + 1)
    if a_prime == 2:
        return True

    elif a_prime % 2 == 0:
            return False

    else:
        for x in range(3, limit+3, 2):
            if a_prime % x == 0:
                # print x
                return False

    return True



def number_of_prime(num):
    #2 is a prime so no_of_primes inital value is 1
    no_of_primes = 1
    for x in range(2, num + 1):
        if prime(x):
            no_of_primes += 1
    print no_of_primes



def _function(a_num, b_num):
    counter_list = []
    prime_list = []
    for a in range(-a_num + 1, a_num):
        for b in range(1, b_num + 1):
            counter = 0
            n = 0
            value = b
            while prime(value) == True:
                n += 1
                value = n**2 + a*n + b
                # print '%d^2 + %d*%d(=%d) + %d = %d: Prime or not: %s: Count: %d'% (n, a, n, a*n, b, value, prime(value), counter)
                counter += 1
                prime_list.append(value)
            counter_list.append('a: %d and b: %d No.Of.Primes: %d' %(a,b,counter))
    return prime_list
    # print counter_list

a_list = _function(2, 41)

for x in a_list:
    if prime(x) == False:
        print prime(x), x















