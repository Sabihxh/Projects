from flpy.excel import convert_excel, rows_to_excel
from flpy.utils import encode_xml

a = './excel/08-Feb-Contacts.xls'
b = './excel/dup-15Feb.xls'
dup_rows = []
singles = []
all_rows = []
emails = []
dup_emails = []

result = convert_excel(b)

for row in result.rows:
    all_rows.append(row)

for row in result.rows:
    mail = row.get('mail')
    emails.append(mail)

#finds all emails that occur more than once and puts them in a list
for mail in emails:
    if emails.count(mail) > 1:
        dup_emails.append(mail)


for row in all_rows:
    for mail in dup_emails:
        if row.get('mail') == mail:
            dup_rows.append(row)
            if '%s'%row in all_rows:
                all_rows.remove('%s'%row)

for row in dup_rows:
    print row.get('mail')


# columns = ['colour', 'ID', 'First Name', 'Last Name', 'mail']# 'Name override',   'For attn. of',    'Salutation'  ,'Organisation'   , 'Position'   , 'Address' ,'Address 1'   ,'Address 2'  , 'Address 3'  , 'Address 4'  , 'Address 5'   ,'Address 6'   ,'Town'   , 'State/County',    'Postcode/Zip' ,   'Country mail' ,   'Main E-mail Label'  , 'Additional E-mails' , 'Main Telephone' , 'Main Telephone Label',    'Fax Number' , 'Additional Tels.' ,   'Additional Addresses' ,   'Website', 'Categories' , 'Interests' ,  'On E-mail List' , 'On Postal Mailing List' , 'Info'  ,  'Purchases' ,      'Custom 1']

# rows_to_excel('./excel/A3-dup-15Feb.xls', new_rows, columns)










