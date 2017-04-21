#This function splits the text file by each line i.e. every line is an element in a list 
def lines_in_list():
    with open('euler_13.txt', 'r') as f:
        line = f.read()
    return line.split('\n')


def add_lines():
    total = 0
    for item in lines_in_list():
        total += int(item)
    print(len(str(total)[0:10]))
    print(str(total)[0:10])
    return str(total)[0:10]

add_lines()
