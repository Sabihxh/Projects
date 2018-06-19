from flpy.excel import convert_excel, rows_to_excel, strip_excel
import os
import shutil
from datetime import datetime as dt
        
"""
Maximum No of columns this script can take is 256 due to rows_to_excel function limit. 
Currently working on increasing this to 500+
"""

def get_file_from_path(a_file):
    split_path = os.path.basename(a_file).rsplit('.', 1)
    file_name = split_path if split_path else ['']
    return file_name[0]


def del_empty_columns(a_file):
    """
    Input: Spreadsheet or Path to Spreadsheet
    Output: Creates a copy of Spreadsheet with empty columns removed
            row_count is a dictionary where column: 1 means that this column has atleast 1
            non-empty row whereas, column: 0 means that all rows in this column are empty
            e.g. del_empty_columns(Workbook1.xls, output_folder = 'formatted_spradsheets'):
    """
    spreadsheet = convert_excel(a_file).rows
    row_count = {column: 0 for column in spreadsheet[0]}
    original_row_col_count = (len(spreadsheet), len(row_count))

    for column in row_count:
        for row in spreadsheet:
            if row.get(column):
                row_count[column] = 1
                break

    list_of_rows = []
    for row in spreadsheet:
        temp_dict = {}
        for column in row_count:
            if row_count[column] == 1:
                temp_dict[column] = row.get(column)
        list_of_rows.append(temp_dict)

    return list_of_rows, original_row_col_count

def del_empty_rows(a_file):
    """
    This function runs after del_empty_columns and depends on it i.e. takes the input from del_empty_columns
    Output: list of dictionaries where an empty dictionary is removed (empty row in spreadsheet)
    """
    list_of_rows = []
    column_formatted = del_empty_columns(a_file)
    for a_dict in column_formatted[0]:
        for key in a_dict:
            if a_dict[key]:
                list_of_rows.append(a_dict)
                break

    modified_row_col_count = (len(list_of_rows), len(list_of_rows[0]))
    return list_of_rows, column_formatted[1], modified_row_col_count

def run_all_spreadsheets(folder = './data/originals'):
    """Returns list of all the xls or xlsx format files from folder"""
    output_folder = 'New_Spreadsheets_%s' % dt.now().strftime('%y%m%d_%H%M%S')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    xls_files = [x for x in os.listdir(folder) if x.endswith('.xls') or x.endswith('.xlsx')]

    for file in xls_files:
        file = folder + '/%s' % file
        list_of_rows = del_empty_rows(file)
        columns = [x for x in list_of_rows[0][0]]
        print "Formatting %s ..." % file
        output_folder_name = './%s/%s.xls' % (output_folder, get_file_from_path(file))
        rows_to_excel(output_folder_name, list_of_rows[0], sorted(columns))

        print "Columns --> before: %s ------ after: %s" % (list_of_rows[1][1], list_of_rows[2][1])
        print "Rows --> before: %s ------ after: %s" % (list_of_rows[1][0], list_of_rows[2][0])
        print 'No of columns removed: %s' % (int(list_of_rows[1][1]) - int(list_of_rows[2][1]))
        print 'No of rows removed: %s' % (int(list_of_rows[1][0]) - int(list_of_rows[2][0]))
        print "Moving to: %s" % output_folder_name
        print '***'*20

run_all_spreadsheets('.')






