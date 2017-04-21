from flpy.excel import rows_to_excel, convert_excel


spreadsheet = convert_excel('Wilkinson_Contacts.xls')
result = []
# for row in spreadsheet.rows:
#     result.append(row)
mega_list = []

for row in spreadsheet.rows:
    mega_list.append(row)

# print mega_list

a_list = []
for row in spreadsheet.rows:
    a_list.append(row.get('mail'))



match_list_101 = []
for row in spreadsheet.rows:
    a_dict = {}
    temp_list = []
    mail = row.get('mail')
    if mail:
        counter = a_list.count(mail)
        if counter > 1:           
            indices = [i for i, x in enumerate(a_list) if x == mail]
            for index in indices:

                temp_list.append(mega_list[index])
    match_list_101.extend(temp_list)




columns = ['ID', 'mail', 'First Name', 'Last Name', 'Name override','For attn. of','Salutation','Organisation','Position',    'Address', 'Address 1',   'Address 2',   'Address 3',   'Address 4',   'Address 5',   'Address 6',   'Town',    'State/County',    'Postcode/Zip',    'Country mail',    'Main E-mail Label',   'Additional E-mails',  'Main Telephone',  'Main Telephone Label',    'Fax Number',  'Additional Tels.',    'Additional Addresses',   'Website', 'Categories',  'Interests',   'On E-mail List',  'On Postal Mailing List',  'Info',    'Purchases',       'Custom 1',    'Custom 2']

rows_to_excel('Duplicate-emails.xls', match_list_101, columns)

# if row.get('mail'):
#     print row.get('mail')









