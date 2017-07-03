from flpy.excel import convert_excel

def get_headers_file(file_path):
    headers_file = 'excel_headers'
    result = convert_excel(file_path).keys
    print result

get_headers_file('inventory_table.xlsx')



