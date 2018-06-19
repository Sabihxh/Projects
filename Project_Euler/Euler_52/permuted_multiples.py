import collections

def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] = d[x] + 1
    for x in b:
        d[x] = d[x] - 1
    return not any(d.itervalues())




def permuted_numbers():
    for x in range(120000, 300000):
        x1, x2, x3, x4, x5, x6 = x, x*2, x*3, x*4, x*5, x*6
        if same_permutation(str(x1), str(x2)) and same_permutation(str(x1), str(x3)) and same_permutation(str(x1), str(x4)) and same_permutation(str(x1), str(x5)) and same_permutation(str(x1), str(x6)):
            print x1, x2, x3, x4, x5, x6

permuted_numbers()