a_string = 'I have <to be deleted> to delete something. And then <again> another one. <This is getting ridiculous>'
def substring(a_string):
    """This function takes a string and deletes anyhting 
    inside <'delete this'>. NOTE: It also removes double spaces from this string. """
    xc = 0
    yc = 0
    index = []
    for x in a_string:
        if x == '<':
            index.append(xc)
            for y in a_string[xc:]:
                yc += 1
                if y =='>':
                    index.append(yc)               
        xc += 1
        yc += 1

    a_string = a_string[:index[0]] + a_string[index[1]:]

    if '<' not in a_string:
        return a_string

    else:
        return substring(a_string)

print substring(a_string).replace('  ', ' ')

