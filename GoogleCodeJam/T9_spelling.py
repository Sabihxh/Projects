a_dict = {
            '0': ' ',
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
key_list = sorted(a_dict)

line = 'hello world'

file = open('./txt_files/large-t9.txt', 'r')

sentences = file.read().split('\n')
print sentences

output_list = []

for line in sentences:
    result = []
    c = 0
    for char in line:

        for key, value in a_dict.items():
            if char.lower() in value:
                position = value.index(char) + 1
                if result and result[-1] == key:
                    result.append(' ')
                for x in range(position):

                    result.append(key)
                    # print char, c
        c += 1
    print ''.join(result)
    output_list.append(''.join(result))

print output_list

out_file = open('./txt_files/output-large-t9.txt', 'w')
c = 1
for x in output_list:
    out_file.write('Case #%s: %s\n'%(c, x))
    c += 1

out_file.close()
file.close()











