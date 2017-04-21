from flpy.excel import convert_excel

result = convert_excel('update-dimensions.xls')

for row in result.rows