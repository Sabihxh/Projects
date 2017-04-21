#The last five years
from flpy.utils import unique_id
from flpy.excel import sql_to_excel

#To make file names unique. 
file_name = 'Test-' + unique_id()  + '.xls'

#Name of the database
database = 'aoldemo2'

#This is the sql command to be used in sql_list
sql_command_1 = """ SELECT 
                ar.soldToid AS 'Sold To ID',                
                fl.firstname AS 'First Name',
                fl.lastname AS 'Last Name',
                fl.directoryOrganisation AS 'Organisation',
                ar.retailPrice AS 'Retail Price'
                FROM
                artworks ar
                INNER JOIN
                fl_interactive_users fl
                ON fl.id = ar.id
                WHERE soldToid != 0;
                """

sql_command_2 = """ SELECT
                id, 
                artist
                FROM
                artworks
                GROUP BY
                artist;
                """

sql_list = [
{
        'worksheet_title': 'All available artworks',
        'sql': sql_command_1,
        'total_columns': [4],
        'col_widths': {0: 1, 1: 3, 2: 3, 3: 5, 4: 5}
        # 'totals_group_by_columns': [4]
    },
    {
        'worksheet_title': 'Artists',
        'sql': sql_command_2,
        'col_widths': {0: 1, 1: 3}
    }
]

sql_to_excel('Test_mine.xls', database, sql_list)
#sql_to_excel('Test.xls', database, sql_list)
#print("Exported as %s" % file_name)
print("Exported as Test_mine.xls")

