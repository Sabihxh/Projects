import math

def _readfile():
    with open("euler_8_string.txt", "r") as f:
        #f1 now has contents of the file (string)
        f1 = f.read()
        #f2 is string with sll spaces removed 
        f2 = "".join(f1.split())
        return f2

#_readfile()

def _multiply():
    #This is where all products of 13 numbers will go
    list_of_products = []
    #last 12 numbers don't need to be multiplied
    for x in range(988):
        
        list_to_mult = []

        for y in range(13):
            k = int(_readfile()[x + y])
            list_to_mult.append(k)

        product = 1    
        for item in list_to_mult:
            product *= item
        list_of_products.append(product)

    return list_of_products


def max_of_list():
    return max(_multiply())

print(max_of_list())

