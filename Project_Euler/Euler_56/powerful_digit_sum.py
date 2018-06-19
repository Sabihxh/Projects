def solution(max_a = 99, max_b = 99):
    max_digit_sum = 1
    for a in range(max_a, 1, -1):
        for b in range(max_b, 1, -1):
            digit_sum = sum(map(int,list(str(a**b))))
            if max_digit_sum < digit_sum:
                max_digit_sum = digit_sum
                print a, b
    return max_digit_sum

print solution()


