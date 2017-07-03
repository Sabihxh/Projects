from flpy.excel import convert_excel, rows_to_excel
from flpy.utils import encode_xml

a = './excel/08-Feb-Contacts.xls'
b = './excel/contacts.xls'

css = convert_excel(b)
result = []
duplicates = []
mega_list = []


emails = []
row_list = []

for c_row in css.rows:
    email = c_row.get('mail')
    if email:
        emails.append(email)
    else:
        emails.append('')

for c_row in css.rows:
    row_list.append(c_row)

to_delete = []

for c_row in css.rows:
    email = c_row.get('mail')
    if email and email != '' and '%s' % email != 'None':
        if email in emails:
            indices = [i for i, x in enumerate(emails) if x == email]
            # print indices
            if len(indices) > 1:
                # print indices
                for index in indices[1:]:
                    if row_list[index].get('colour') == 'r':
                        to_delete.append(index)
                        # print row_list[indices[0]]['On E-mail List']
                        row_list[indices[0]]['On E-mail List'] = 'Y'
                        # print row_list[indices[0]]['On E-mail List']
   

to_delete = sorted(list(set(to_delete)))[::-1]

for x in to_delete:
    # print 'deleted: ', x
    del(row_list[x])

for x in to_delete:
    # print 'deleted: ', x
    del(emails[x])


single_email_indexes = []
filtered_list = []
sorted_email_index_list = []
dup_email_indexes = []

for email in emails:
    if email and email != '0000':
        indexes = [i for i, x in enumerate(emails) if x == email]
        if len(indexes) > 1:
            dup_email_indexes.extend(indexes)
        else:
            single_email_indexes.extend(indexes)

        for index in indexes:
            emails[index] = '0000'

    elif email == '':
        single_email_indexes.append()


all_indexes = dup_email_indexes + single_email_indexes


##############################################



columns = ['colour',   'ID',  'First Name',  'Last Name', 'mail',  'Name override',   'For attn. of',    'Salutation'  ,'Organisation'   , 'Position'   , 'Address' ,'Address 1'   ,'Address 2'  , 'Address 3'  , 'Address 4'  , 'Address 5'   ,'Address 6'   ,'Town'   , 'State/County',    'Postcode/Zip' ,   'Country mail' ,   'Main E-mail Label'  , 'Additional E-mails' , 'Main Telephone' , 'Main Telephone Label',    'Fax Number' , 'Additional Tels.' ,   'Additional Addresses' ,   'Website', 'Categories' , 'Interests' ,  'On E-mail List' , 'On Postal Mailing List' , 'Info'  ,  'Purchases' ,      'Custom 1']

rows_to_excel('./excel/dup-15Feb-A2.xls', new_rows, columns)




