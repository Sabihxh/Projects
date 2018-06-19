def solution():
    _sum = 0
    for x in range(1, 10001):
        value =  pow(x, x)
        _sum += value
    return str(_sum)[len(str(_sum)) - 10:]
print(solution())


def solution_2():
    return str(sum(map(lambda x: pow(x, x), range(1, 10001))))[-10:]
print(solution_2())

