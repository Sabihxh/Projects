#The last five years
from flpy.utils import unique_id
from flpy.excel import sql_to_excel

#To make file names unique. 
file_name = 'Test-' + unique_id()  + '.xls'

#Name of the database
database = 'inglebygallery'

#This is the sql command to be used in sql_list
sql_command_1 = """ SELECT 
                    CONCAT(lastname, ', ', firstname) clf, 
                    email AS 'Email', 
                    COUNT(*) AS 'Repeated' 
                    FROM fl_interactive_users 
                    GROUP BY CONCAT(lastname, ', ', firstname)
                    HAVING COUNT(*) > 1;
                """

sql_command_2 = """SELECT 
                    firstname, 
                    lastname, 
                    fl_interactive_users.email 
                    from 
                    fl_interactive_users 
                    INNER JOIN 
                        (SELECT email 
                        FROM 
                        fl_interactive_users 
                        GROUP BY email 
                        HAVING count(email) > 1) dup 
                    ON fl_interactive_users.email = dup.email;"""

sql_command_3 = """SELECT fullname, email, creationdate, count(*) FROM fl_interactive_users GROUP BY CONCAT(lastname, firstname) HAVING COUNT(*) > 1 ORDER BY lastname;"""


sql_list_3 = [
{
        'worksheet_title': 'Duplicates',
        'sql': sql_command_3,
        'col_widths': {0: 5, 1: 5, 2: 2}
    }
]


sql_list_2 = [
{
        'worksheet_title': 'Duplicates',
        'sql': sql_command_2,
        'col_widths': {0: 5, 1: 5, 2: 2}
    }
]

# sql_to_excel('email_dup.xls', database, sql_list_2)
sql_to_excel('email_dup.xls', database, sql_list_3)
print 'Done'

