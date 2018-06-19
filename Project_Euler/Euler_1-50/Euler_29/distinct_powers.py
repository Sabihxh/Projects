# Euler 29
def a_power_b(range_1, range_2):
    result = []
    for a in range(range_1, range_2 + 1):
        for b in range(range_1, range_2 + 1):
            value = a ** b
            if value not in result:
                result.append(value)

    return len(result)

print a_power_b(2, 100)


