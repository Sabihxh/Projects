# filepath = './txt_files/small.txt'

def number_of_cases(filepath):
    price_list = []
    a_file = int(open(filepath, 'r').readline())
    return a_file



def price_list(filepath):
    price_list = []

    a_file = open(filepath, 'r').read().split('\n')
    a_len = len(a_file)
    
    for x in range(3, a_len, 3):
        price_list.append(a_file[x])
    
    return price_list


def price_dict(filepath):
    result = []
    price_list = []
    target_list = []
    
    a_file = open(filepath, 'r').read().split('\n')
    a_len = len(a_file)
    
    for x in range(3, a_len, 3):
        price_list.append(a_file[x])
        

    for x in range(1, a_len, 3):
        target_list.append(a_file[x])
        
    price_dict = {'Case #%s' % (int(x) + 1): y for x, y in enumerate(price_list)}
    return price_dict


def price_case_list(filepath):
    result = []
    price_list = []
    target_list = []
    
    a_file = open(filepath, 'r').read().split('\n')
    a_len = len(a_file)
    
    for x in range(3, a_len, 3):
        price_list.append(a_file[x])
        

    for x in range(1, a_len, 3):
        target_list.append(a_file[x])
        
    price_dict = {'Case #%s' % (int(x) + 1): y for x, y in enumerate(price_list)}

    for key, value in sorted(price_dict.items()):
        result.append('%s: %s' % (key, value))        

    return result




def target_list(filepath):
    target_list = []
    
    a_file = open(filepath, 'r').read().split('\n')
    a_len = len(a_file)    

    for x in range(1, a_len, 3):
        target_list.append(a_file[x])
    target_list = map(int, target_list)
    return target_list

# print number_of_cases(filepath)
# print price_dict(filepath)
# print price_list(filepath)
# print target_list(filepath)























