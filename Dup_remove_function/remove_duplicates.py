from flpy.db.connection import execute as _execute
from flpy.excel import convert_excel
import random
a_file = open('random_emails.txt', 'w')
a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
random.choice(a)
for x in range(25000):
    a_string = ''
    for y in range(20):
        a_string += random.choice(a)
    a_file.write('%s\n'%a_string)
a_file.close()

result = convert_excel('test_large_file.xls')
a_list = []

for row in result.rows:
    a_list.append(row)

print len(a_list)

def output_non_duplicates(list_of_dicts):
    existing_emails = set()
    #Gets all the existing emails in from database and puts it in a set
    result = _execute('mbla', "SELECT email FROM fl_interactive_users WHERE email <>''")
    for row in result.rows:
        email = row.get('email')
        existing_emails.add(email)

    #This is the output list which will not have any duplicates
    output_list = []

    for row in list_of_dicts:
        if row.get('E-mail') not in existing_emails:
            output_list.append(row)

    return output_list

output_non_duplicates(a_list)


