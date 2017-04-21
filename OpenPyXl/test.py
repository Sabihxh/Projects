from flpy.excel import strip_excel, convert_excel

# for row in convert_excel('./excel/testlower.xls').rows:
#     print row
strip_excel('./excel/testtest.xlsx', './excel/output1.xlsx', ignore_cell_if = lambda x: x == '')

