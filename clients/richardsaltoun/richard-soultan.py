from flpy.excel import convert_excel, rows_to_excel



dim = convert_excel('update-dimensions.xls')
new_file = convert_excel('inch_to_cm.xls')

row_list = []
for row in dim.rows:
    
    a_list = []

    initial_list = row.get('Size in inches').split('x')
    for x in initial_list:

        value = x.replace('in', '')
        value = float(value.replace(' ', ''))
        centi = value * 2.54
        a_list.append(centi)

    value = '%s x %s cm' % (a_list[0], a_list[1])
    row_list.append({'Stock Number': row.get('Stock Number'), 'Dimensions': '%s\\n%s' % (row.get('Size in inches'), value)})
    print row_list

columns = ['Stock Number', 'Dimensions']
rows_to_excel('inch_to_cm.xls', row_list, columns)

file = open('output-update-dimensions.sql', 'w')
for row in new_file.rows:
    file.write("UPDATE artworks set dimensions = '%s' WHERE stockNumber = '%s';\n" % (row.get('Dimensions'), row.get('Stock Number')))

file.close()