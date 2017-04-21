import math

#Reads text file containing the grid and puts it in a list
def _file_to_list():
    with open('Euler_11.txt', 'r') as reader:
        _string = reader.read()

    _string = _string.split()

    for i in range(20,420,20):
        _string.insert(i, '00')
    # print _string
    return _string



def _largest_num_2():
    num = _file_to_list()
    largest = 0
    for i in range(337):
        product = int(num[i + 0]) * int(num[i + 22]) * int(num[i + 43]) * int(num[i + 64])
        if product > largest:
            largest = product


    for i in range(340):
        product = int(num[i + 0]) * int(num[i + 20]) * int(num[i + 40]) * int(num[i + 60])
        if product > largest:
            largest = product


    for i in range(397):
        product = int(num[i + 0]) * int(num[i + 1]) * int(num[i + 2]) * int(num[i + 3])
        if product > largest:
            largest = product


    for i in range(336, 337):
        product = int(num[i + 3]) * int(num[i + 22]) * int(num[i + 41]) * int(num[i + 60])
        if product > largest:
            largest = product   

    print largest



_largest_num_2()







