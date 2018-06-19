def is_prime(a_num):
    limit = int(a_num/2 + 1)
    
    if a_prime == 2:
        return True

    else:
        for x in range(3, limit+3, 2):
            if a_prime % x == 0:
                # print x
                return False

    return True

def find_prime():
    for i in range(100):
        if i