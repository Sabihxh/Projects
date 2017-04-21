from filepaths_store_credits import price_dict, price_list, target_list, number_of_cases

filepath = './txt_files/small.txt'

def index_finder(c, a_list):

    result = []

    for a in a_list:
        for b in a_list:

            if a + b == c and  a_list.index(b) != a_list.index(a):
                index_list = [(x + 1) for x, y in enumerate(a_list) if y == a or y == b]
                return index_list

            elif a + a == c and len([(x + 1) for x, y in enumerate(a_list) if y == a]) >= 2:

                index = [(x + 1) for x, y in enumerate(a_list) if y == a]
                if a_list[index[0] - 1] + a_list[index[1] - 1] == c:
                    return index

# index_finder(8, [2, 1, 9, 4, 4, 56, 90, 3])

def store_credit(filepath):
    limit = number_of_cases(filepath)
    targets = target_list(filepath)

    result = []
    checker = []
    for num in range(limit):

        p_list = map(int, price_list(filepath)[num].split())
        c = targets[num]
        
        if index_finder(c, p_list):
            result.append('Case #%s: %s' % (num + 1, ' '.join(map(str, index_finder(c, p_list)))))
        else:
            result.append('Case #%s: ' % (num + 1))
    return result

# store_credit(filepath)
filepath = './txt_files/small.txt'

def small_output_file(filepath):
    file = open('./txt_files/small_output.txt' , 'w')
    for case in store_credit(filepath):
        file.write('%s\n' % case)

    file.close()

small_output_file(filepath)


filepath = './txt_files/large.txt'

def large_output_file(filepath):
    file = open('./txt_files/large_output.txt' , 'w')
    for case in store_credit(filepath):
        file.write('%s\n' % case)
    file.close()

large_output_file(filepath)

