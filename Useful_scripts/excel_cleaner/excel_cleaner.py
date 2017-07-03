from flpy.excel import convert_excel, rows_to_excel
from flpy.utils import encode_xml
import codecs
import csv


"""
Given a spreadsheet, 
remove all blank columns from this spreadsheet
"""


def get_headers_file(file_path):
    spreadsheet = convert_excel(file_path)
    
    data_file = codecs.open('cleaned_spreadsheet.csv', 'w', 'utf-8')

    #Gets all the column names from spreadsheet and puts them in dictionary with 0 as default value
    dict_with_headers = {x: 0 for x in spreadsheet.keys}
    
    for row in spreadsheet.rows:
        for header, count in dict_with_headers.items():
            if row.get(header):
                dict_with_headers[header] += 1

    set_of_nonempty_columns = []
    for header in dict_with_headers:
        if dict_with_headers[header] > 0:
            set_of_nonempty_columns.append(header)

    list_of_dicts = []
    for row in spreadsheet.rows:
        dict_of_nonempty_columns = {}

        for column in set_of_nonempty_columns:

            value = '%s'%row.get(column)
            if value:
                value = value.encode('utf-8')
            dict_of_nonempty_columns[column] = value

        list_of_dicts.append(dict_of_nonempty_columns)

    with open('cleaned_spreadsheet.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = set_of_nonempty_columns)
        writer.writeheader()
        for a_dict in list_of_dicts:
            writer.writerow(a_dict)


    # rows_to_excel('cleaned_spreadsheet.xls', list_of_dicts,  sorted(set_of_nonempty_columns))


def get_headers_file_2(file_path):
    spreadsheet = convert_excel(file_path)
    output_filename = file_path.split('.')[0]
    data_file = codecs.open('%s-cleaned.csv' % output_filename, 'w', 'utf-8')

    #Gets all the column names from spreadsheet and puts them in dictionary with 0 as default value
    dict_with_headers = {x: 0 for x in spreadsheet.keys}
    
    for row in spreadsheet.rows:
        for header, count in dict_with_headers.items():
            if row.get(header):
                dict_with_headers[header] += 1

    set_of_nonempty_columns = []
    for header in dict_with_headers:
        if dict_with_headers[header] > 0:
            set_of_nonempty_columns.append(header)

    list_of_dicts = []
    for row in spreadsheet.rows:
        dict_of_nonempty_columns = {}

        for column in set_of_nonempty_columns:

            value = '%s'%row.get(column)
            if value:
                value = value.encode('utf-8')
            dict_of_nonempty_columns[column] = value

        list_of_dicts.append(dict_of_nonempty_columns)

    with open('cleaned_spreadsheet.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = set_of_nonempty_columns)
        writer.writeheader()
        for a_dict in list_of_dicts:
            writer.writerow(a_dict)

get_headers_file('clean_test.xlsx')














