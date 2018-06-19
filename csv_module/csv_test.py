import csv
import sys
from flpy.excel import rows_to_excel

csv.field_size_limit(sys.maxsize)
# with open('csv_file_chars.csv', 'wb') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Hey, how are you doing?', 'Mike,\nI am fine thanks'])
#     csv_writer.writerow(['Its been a while "Nancy", perhaps a coffee this saturday?', 'Yea, that sounds nice, how about 10am?'])

# with open('csv_file_chars.csv', 'rb') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         pass

def parameters_to_change():
    a_file = '/Users/artlogic/Desktop/Galleries/SadieColes/13Nov_Data/web-app-exports/sadie-coles-artists.csv'
    return a_file


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


def csv_to_list():
    a_file = parameters_to_change()
    a_list = []

    with open(a_file, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file)
        # headers = next(csv_reader)    
        for row in csv_reader:
            a_list.append(row)

    return a_list


def list_to_csv():
    a_file = 'list_to_csv.csv'
    data = csv_to_list()
    with open(a_file, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file)
        for x in data:
            print type(x[0])
            csv_writer.writerow(x)

list_to_csv()
# rows_to_excel('csv_to_excel.xls', [{1:'Hey'}], [1])













