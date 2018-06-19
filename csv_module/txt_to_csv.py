import csv
import codecs
import io
import sys
from flpy.excel import rows_to_excel
import execute

        

input_file = open('EDITED_EXPORT_DECEMBER.csv')


txt_file = r"EDITED_EXPORT_DECEMBER.txt"
csv_file = open('mycsv.csv', 'w')
csv_writer = csv.writer(csv_file)


open_file = codecs.open(txt_file, encoding='utf-16')
file_read = open_file.read()
file_list = file_read.split('\r')
for line in file_list:
    line_list = line.split('\t')
    print line_list, len(line_list)
    print '***' * 30
    line_list_encoded = [x.replace('\n', '<n>').encode('utf-8') for x in line_list]
    csv_writer.writerow(line_list_encoded)




# pd.read_csv('mycsv.csv').to_excel('juergan_excel.xlsx')

# if we read f.csv we will write f.xlsx
# wb = xlsxwriter.Workbook(sys.argv[1].replace(".csv",".xlsx"))
# ws = wb.add_worksheet("WS1")    # your worksheet title here
# with open(sys.argv[1],'r') as csvfile:
#     table = csv.reader(csvfile)
#     i = 0
#     # write each row from the csv file as text into the excel file
#     # this may be adjusted to use 'excel types' explicitly (see xlsxwriter doc)
#     for row in table:
#         print row
#         ws.write_row(i, 0, row)
#         i += 1

# wb.close()



