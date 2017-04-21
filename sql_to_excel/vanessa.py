from flpy.excel import sql_to_excel

sql_command = ('SELECT soldtoid, soldto, saledate FROM artworks WHERE soldto LIKE \'Vanessa%\';')

sql_to_excel('Vanessa.xls', 'aoldemo2', sql_command)

print('Exported to: Venessa.xls')

