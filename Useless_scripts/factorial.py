def factorial(x):
    total = 1
    for num in range(1, x+1):
        total *= num
    return total
print factorial(0)

a_num = 145
total = 0
curious_nums = []
for a_num in range(11, 999999):

    total = 0
    a_list = list('%s'%a_num)
    for x in a_list:
        total += factorial(int(x))

    if total == a_num:
        curious_nums.append(a_num)

print curious_nums
