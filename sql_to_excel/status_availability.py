# Questions: How do I display 'Stock' and 'On Consignment' instead of '1' and '2'. 

from flpy.excel import sql_to_excel
from aolpy.prefs import get_prefs
from flpy.database import execute
from flpy.excel import rows_to_excel

#Name of the database
database = 'aoldemo2'

#Get the main dictionary 
prefs = get_prefs('artlogiconline')
# print(prefs.mappings.statuses.get('1'))
print(prefs.mappings.availabilities)
#Get the status
in_stock = prefs.mappings.statuses.get('1')


sql_command_stock = """SELECT 
                        id, 
                        status 
                        FROM 
                        artworks 
                        WHERE status = 1"""

sql_command_consignment = """SELECT 
                            id, 
                            status 
                            FROM 
                            artworks 
                            WHERE status = 2"""


results = execute(database, sql_command_stock )



sql_list = [
    {
        'worksheet_title': 'Artworks in Stock',
        'sql': sql_command_stock,
        'data': None,
        'col_widths': {1: 2},
        'total_columns': [],
    },
    {
        'worksheet_title': 'Artworks on Consignment',
        'sql': sql_command_consignment,
        'data': None,
        'col_widths': {0:2},
        'total_columns': [],
    }
]
sql_to_excel('status_availability.xls', database, sql_list)

print('Created: status_availability.xls')








