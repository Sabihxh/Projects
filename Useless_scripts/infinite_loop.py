import string, random, os.path
from flpy.excel import convert_excel, rows_to_excel

# a = [{'id': 1}, {'id': 2}]
# rows_to_excel('Test.xls', a, ['id'])

#create a list of dicts then use rows_to_excel to fill a column with mix data


num = 20

#This function takes num as its arguement and produces that many random email addresses
def email_generator(num):
    email_list = []
    domain_names = ['hotmail', 'artlogic', 'gmail']
    ends = ['.co.uk', '.com', '.net', '.org']
    for x in range(num):

        email = ''
        email_length = random.randrange(5,12)
        for length in range(email_length):
            #Only generates random string with lower case, maybe I cna make it better?
            email += random.choice(string.letters[0:26])

        email += '@%s%s' % (random.choice(domain_names), random.choice(ends))
        email_list.append(email)
    return email_list

#generates random mobile numbers, 'num' many of them
def mobile_no_generator(num):
    mobile_list = []
    for x in range(num):
        mobile_no = ''
        for x in range(9):
            mobile_no += '%d'%random.randrange(0,10)
        mobile_no = '07' + mobile_no
        mobile_list.append(mobile_no)
    return mobile_list


#takes a string 'key' and a list, returns a list of dicts with each element in
#original key as a key:value in new dict e.g. 
#convert_to_dict('ID', [1,2,3]) will return [{'ID': 1},{'ID': 2}, {'ID': 3}]
#This can be used in conjunction with convert_excel
def convert_to_dict(key, a_list):
    final_list = []
    for item in a_list:
        a_dict = {}
        a_dict[key] = item
        final_list.append(a_dict)
    return final_list

#Creates a list with both numbers and emails
def mobiles_emails(num):
    mobiles = mobile_no_generator(num)
    emails = email_generator(num)
    return mobiles + emails



#Now need to filter the data
#find emails and put them in a seperate column

def filter_data(num):
    data_list = mobiles_emails(num)
    main_list = []
    for data in data_list:
        a_dict = {'emails': '', 'mobiles': ''}
        if '@' in data:
            a_dict['emails'] = data

        else:
            a_dict['mobiles'] = data
        main_list.append(a_dict)
    return main_list



rows = filter_data(num)
sheet_name = 'Test.xls'
rows_to_excel(sheet_name, rows, ['emails', 'mobiles'])
print '%s: Created path...file path %s' % (sheet_name, os.path.abspath('Test.xls'))






















