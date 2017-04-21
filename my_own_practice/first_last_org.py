import os
from flpy.database import execute

output_file = 'pkg-indexedsort-update-NEW.txt'
db = 'pkg'
sql = "SELECT id, firstName, lastName, directoryOrganisation, indexedSort FROM fl_interactive_users WHERE indexedSort = '' AND listSource = 'Artlogic Import 20161107 DG(Dennis)'"


result_file = open(output_file, 'w')
results = execute(db, sql)

fields_to_include = ['lastName', 'firstName', 'directoryOrganisation']

if results:
    for row in results.rows:
        a_list = []
        rec_id = row.get('id')


        for field in fields_to_include:
            if row.get(field):
                a_list.append(row.get(field))


        indexedSort = ' '.join(a_list)

        # update_sql_template = "UPDATE fl_interactive_users SET indexedSort='%%(first_name)s' WHERE id=%s" % id
        # result_file.write(update_sql_template % {'first_name' : first_name} + '\n')

        if indexedSort:
            update_sql_template = "UPDATE fl_interactive_users SET indexedSort='%%(index_sort)s' WHERE id=%s" % rec_id
            result_file.write(update_sql_template % {'index_sort' : indexedSort} + '\n')


result_file.close()
print('Created output file: %s' % output_file)

        # BUILD YOUR SQL HERE. THIS IS JUST AN EXAMPLE
        # if row.get('firstName') and row.get('lastName') and row.get('directoryOrganisation'):
        #     a_list.extend([row.get('lastName'), row.get('firstName'), row.get('directoryOrganisation')])

        # elif row.get('firstName') and row.get('lastName'):
        #     a_list.extend([row.get('lastName'), row.get('firstName')])

        # elif row.get('lastName') and row.get('directoryOrganisation'):
        #     a_list.extend([row.get('lastName'), row.get('directoryOrganisation')])

        # elif row.get('firstName') and row.get('directoryOrganisation'):
        #     a_list.extend([row.get('firstName'), row.get('directoryOrganisation')])

        # elif row.get('firstName'):
        #     a_list.append(row.get('firstName'))

        # elif row.get('lastName'):
        #     a_list.append(row.get('lastName'))

        # elif row.get('directoryOrganisation'):
        #     a_list.append(row.get('directoryOrganisation'))
        # a_string = ' '.join(a_list)
