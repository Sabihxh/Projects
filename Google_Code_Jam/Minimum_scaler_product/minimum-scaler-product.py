#Finds scaler product given vectors in list
sample = 'sample.txt'
small = 'small.txt'
large = 'large.txt'
def scaler_product(a_list, b_list):
    total = 0
    for x in range(len(a_list)):
        total += a_list[x] * b_list[x]
    return total

# print scaler_product([1,3,-5], [1,-2,4])

a = sorted([1,2,3,4,5])
b = sorted([1,0,1,0,1], reverse = True)

# print scaler_product(sorted(a), sorted(b, reverse = True))

def minimum(a_list, b_list):
    mini = scaler_product(sorted(a_list), sorted(b_list, reverse = True))
    return mini

# print minimum(a, b)

#makes it [ [[a],[b]], [[c],[d]] ] 
def input_small(filepath):
    file = open(filepath, 'r')
    true_file = file.read().split('\n')
    # print true_file
    count = len(true_file)
    list_of_list = []
    mul_3 = [x for x in range(3, count, 3)]
    all_nums = [x for x in range(1, count)]
    true_list = [x for x in all_nums if x not in mul_3]
    # print true_list
    for x in true_list:
        # print x
        list_of_list.append(true_file[x])
    # print list_of_list

    list_of_list.reverse()
    count = len(list_of_list)
    true_list_pair = []
    for x in range(0, count, 2):
        list_pair = []
        list_pair.append(list_of_list.pop())
        
        list_pair.append(list_of_list.pop())
        
        true_list_pair.append(list_pair)

    truly_true_list_pair = []
    for pair in true_list_pair:
        truly_true_list_pair.append([pair[0].split(), pair[1].split()])
    return truly_true_list_pair




def finally_ey(filepath):
    result = []
    list_of_list = input_small(filepath)
    for pair_list in list_of_list:
        # print pair_list[0], pair_list[1]
        result.append(minimum(map(int, pair_list[0]), map(int, pair_list[1])))
    return result

# print finally_ey('sample.txt')

def output_format(filepath):
    cases = finally_ey(filepath)
    result = []
    c = 1
    for case in cases:
        result.append('Case #%s: %s' %(c, case))
        c += 1
    return result

# print output_file(sample)

def small_output(filepath):
    file = open('small-output.txt', 'w')
    for x in output_format(filepath):
        file.write('%s\n' % x)
    file.close()

small_output(small)

def large_output(filepath):
    file = open('large-output.txt', 'w')
    for x in output_format(filepath):
        file.write('%s\n' % x)
    file.close()

large_output(large)











