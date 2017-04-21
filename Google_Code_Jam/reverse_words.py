a = 'reverse this is'
path_to_file = './txt_files/reverse_large.txt'

def fileOps(path_to_file):
    file = open(path_to_file, 'r')
    a_list = file.read().split('\n')[1:]
    return a_list

# print fileOps(path_to_file)

def reverser(sentence):
    reverse = ' '.join(sentence.split()[::-1])
    return reverse

# print reverser(a)

def reverse_all(path_to_file):
    result = []
    for sentence in fileOps(path_to_file):
        result.append(reverser(sentence))

    return result

# print reverse_all(path_to_file)

def output_file(path_to_file):
    output = open('./txt_files/rev_sol_large.txt', 'w')
    c = 1
    for sentence in reverse_all(path_to_file):
        output.write('Case #%s: %s\n'% (c, sentence))
        c += 1

    output.close()

output_file(path_to_file)