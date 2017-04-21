from aolpy.sql.artwork import artwork_sql
from flpy.utils import display_date

from aolpy.prefs import get_prefs

from flpy.utils import unique_id
#import sql_to_excel method from flpy.excel
from flpy.excel import rows_to_excel
from flpy.database import execute

output_file = 'my-sql-rows_to_excel-test-%s.xls' % unique_id()
database = 'aoldemo2'

columns = [
    'id', 
    'status',
    'availability',
    'Testing'
]

sql_command = """SELECT 
    id,
    status,
    availability
    FROM 
    artworks
"""
prefs = get_prefs('artlogiconline')

results = execute(database, sql_command)
if results:
    for row in results.rows: 
        row['Testing'] = 'HELLO'

rows_to_excel('Test_mine.xls', results.rows, columns)

print("Created export: Test_mine.xls")
#print("Created  export: %s" %output_file)


