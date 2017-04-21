from flpy.excel import rows_to_excel, convert_excel

result = convert_excel('google_doc.xls')

main_list = []

for row in result.rows:
    row['AOL2'] = 'https://secure.artlogiconline.com/%s' % row.get('Shot name')
    row['AOL3'] = 'https://app.artlogic.net/%s' % row.get('Shot name')

    main_list.append(row)
columns = ['Shot name', 'Long name', 'Check by', 'Complete', 'AOL2', 'AOL3']
rows_to_excel('Clients.xls', main_list, columns)