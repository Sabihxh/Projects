def combination_finder(grid):
    grid_2 = 2*grid + 1
    product_l = 1
    product_s = 1
    combination = 0
    for x in range(grid + 1, grid_2):
        product_l *= x
    for x in range(1, grid + 1):
        product_s *= x
    combination = product_l/product_s
    print(combination)

combination_finder(20)
