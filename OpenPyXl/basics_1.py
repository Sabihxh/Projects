from openpyxl import Workbook
from openpyxl.compat import range 
from openpyxl.utils import get_column_letter
from datetime import datetime


wb = Workbook()

ws = wb.active


ws.append([1, 2, 3])
ws['A2'] = datetime.now()
ws['B2'] = '42'


wb.save('./excel/test.xlsx')
print 'file created'