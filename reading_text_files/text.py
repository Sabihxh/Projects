okay = open('./text_files/category.txt')
category = okay.read()
# print category

okay = open('./text_files/gcategory.txt')
gcategory = okay.read()
# print gcategory

okay = open('./text_files/category2.txt')
category2 = okay.read()

list_1 = category.split('\n')
list_g = gcategory.split('\n')
list_2 = category2.split('\n')

for x in list_2:
    if x not in list_1 and x not in list_g:
        print x