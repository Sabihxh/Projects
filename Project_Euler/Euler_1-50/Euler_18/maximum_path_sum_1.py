triangle_num = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

table = [map(int, s.split()) for s in open('triangle.txt', 'r').readlines()][0:-1]
# print len(a_list)
for row in range(len(table)-1, 0, -1):
    for col in range(row):
        table[row - 1][col] += max(table[row][col], table[row][col + 1]) 
        # print table[row - 1][col]
print table















# table = [map(int, s.split()) for s in open('triangle.txt').readlines()][0:-1]

# for row in range(len(table)-1, 0, -1):
#     for col in range(0, row):
#         table[row-1][col] += max(table[row][col], table[row][col + 1])
# print table[0][0]





















# for line in triangle:
#     rows.append([int(i) for i in line.rstrip('\n').split(" ")])
# print rows

#list_of_lists returns each row as a list...
# def list_of_lists():
#     a_list = triangle.split('\n')[1:-1]
#     mega_list = []
#     for x in a_list:
#         y = x.split(' ')
#         mega_list.append(y)
#     return mega_list

# # print(list_of_lists()

# def sum_it_up():
#     a_list = list_of_lists()
#     for x in range(15):
#         pass
        
# sum_it_up()

# testing = [[1], [1,2], [1,2,3], [1,2,3,4]]

# for i in range(4):





# for sec_list in range(len(testing[-2])):
#     #number of elements in last list
#     for j in range(len(testing[-1])):
#         sums = testing[0][0] + testing[1][0] + testing[2][sec_list] + testing[3][j]
#         print '%s + %s + %s + %s' % (testing[0][0], testing[1][0],testing[2][sec_list], testing[3][j])
#         print sums



















