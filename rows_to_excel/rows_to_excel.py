from aolpy.sql.artwork import artwork_sql
from flpy.utils import display_date

from flpy.utils import unique_id
#import sql_to_excel method from flpy.excel
from flpy.excel import rows_to_excel
from flpy.database import execute

output_file = 'my-sql-rows_to_excel-test-%s.xls' % unique_id()
database = 'aoldemo2'
#These column names must match up with SELECTED columns in sql command,
#but these can be more
#Names must match however, you can order however you want here. and create extra columns
columns = [
    'id', 
    'stockNumber', 
    'artist', 
    'artistSort', 
    'title', 
    'artistSortTitleYear', 
    'Medium', 
    'Dimensions', 
    ('signedAndDated', 'Signed and dated'), 
    'Provenance', 
    'Literature', 
    'Exhibitions',
    'edition_details', 
    'is_edition', 
    'editionDetails',
    'testing',
    'creation_date'
]

sql_command = """SELECT 
    id, 
    stockNumber, 
    artist, 
    artistSort, 
    title, 
    artistSortTitleYear, 
    Medium, 
    Dimensions, 
    signedAndDated, 
    Provenance, 
    Literature, 
    Exhibitions,
    %s AS edition_details, 
    IF(isEdition = 1, 'YES', 'No') AS is_edition , 
    editionDetails,
    creationDate
    FROM 
    artworks 
    WHERE creationDate != 0;
""" % artwork_sql.edition_number_sql

results = execute(database, sql_command)
print results.rows
if results:
    for row in results.rows:
        row['testing'] = 'HELLO'
        row['creation_date'] = display_date(row.get('creationDate'),True)
        # print(display_date(row.get('creationDate'),True))




rows_to_excel('Test_mine.xls', results.rows, columns)

print("Created export: Test_mine.xls")
#print("Created  export: %s" %output_file)


