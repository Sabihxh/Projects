from openpyxl import Workbook
from openpyxl.compat import range 
import openpyxl.utils
import random
from datetime import datetime

rand_num = random.randrange(1, 10)

dest_file = './excel/test.xlsx'

wb = Workbook()
ws1 = wb.active

ws1.title = "Range names"

print rand_num
for row in range(1, 40):
    ws1.append(range(rand_num))

print rand_num

wb.save(filename = dest_file)