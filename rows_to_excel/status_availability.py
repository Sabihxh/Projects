from aolpy.sql.artwork import artwork_sql
from flpy.utils import display_date

from aolpy.prefs import get_prefs
from flpy.utils import unique_id
#import sql_to_excel method from flpy.excel
from flpy.excel import rows_to_excel
from flpy.database import execute

database = 'aoldemo2'

columns = [
    'id',
    '__Status',
    '__Availability'
]

sql_command = """SELECT 
    id,
    status,
    availability
    FROM artworks;
"""
results = execute(database, sql_command)
#What does result.rows do?
#If result is not empty
prefs = get_prefs('artlogiconline')
#print(prefs.mappings.statuses)
# s = prefs.mappings.statuses
#print(s.get('1'))

s = prefs.mappings.statuses
a = prefs.mappings.availabilities
print '\n'
print s
print '\n'
print a


# print(a.get('2'))

#print(prefs.mappings.statuses.get(row.get('status')))

#Why is it printing out none?
if results:
    for row in results.rows:
        
        #status_key = row.get('status')
        #status_key_string ='%s' % status_key
        _status = prefs.mappings.statuses.get('%s' % row.get('status', ''))
        _availability = prefs.mappings.availabilities.get('%s' % row.get('availability', ''))
        row['__Status'] = '%s' % _status
        #row['Availability'] = '%s' % _availability
        row['__Availability'] = '%s' % _availability
        #print(type(status_key_string))
        #print(status_key_string)
        #row['creation_date'] = row.get('creationDate')
#print(get_prefs('artlogiconline'))

rows_to_excel('Test_mine_1.xls', results.rows, columns)

print("Created export: Test_mine_1.xls")







