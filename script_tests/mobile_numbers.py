
a_list = ['07726372637abs', '12345928392', 'agr8', '83484232332837']
for value in a_list:
    count = 0
    for char in value:
        if char.isdigit():
            count += 1
    if count >= 9:
        return value