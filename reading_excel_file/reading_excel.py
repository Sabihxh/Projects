# #For reading excel files
# import openpyxl

# #loads the workbook and lets it equal to wb
# wb = openpyxl.load_workbook('Exercise_1.xls')

# #This prints the name of sheet
# print(wb.get_sheet_names())

# sheet = wb.get_sheet_by_name('Sheet1')

# sheet['A1']

from flpy.excel import rows_to_excel, convert_excel
from collections import defaultdict


artworks = convert_excel('Exercise_1.xls')

# a_dict = {'Status': '', 'Acquired': '', 'Active': ''}
a_dict = {}
spreadsheet = []
a_spreadsheet = []
a_list = ['Available' ]
inven_list = []
# d = {defaultdict(int)}

main_dict = {}
for row in artworks.rows:
    dictionary_key = '%s-%s-%s'%(row.get('Status') , row.get('Acquired'), row.get('Active'))
    if dictionary_key not in main_dict:
        print(type(row.get('Acquired')))
        main_dict[dictionary_key] = {'Status': '%s'%(row.get('Status')), 'Acquired': '%s'%(row.get('Acquired')), 'Active': row.get('Active'), 'n_works' : 1, 'InventoryNum': [row.get('InventoryNum')]}

    else:
        if len(main_dict[dictionary_key]['InventoryNum']) <= 7:
            main_dict[dictionary_key]['InventoryNum'].append(row.get('InventoryNum'))
        main_dict[dictionary_key]['n_works'] += 1

spreadsheet = []
for key in main_dict.keys():
    main_dict[key]['InventoryNum'] = ', '.join(main_dict[key]['InventoryNum'])
    spreadsheet.append(main_dict[key])

print(len(spreadsheet))


rows_to_excel('map.xlsx', spreadsheet, ['Status', 'Acquired', 'Active', 'n_works', 'InventoryNum'])




map = {}

key_columns = ['Acquired','Active','Status']

for row in artworks.rows:
    combination = []
    for key in key_columns:
        combination.append(row.get(key) or '')
    combination = ('-'.join(combination)).lower()
    if combination not in map:
        examples = []
        if row.get('InventoryNum') and row.get('InventoryNum').strip() != '':
            examples.append(row.get('InventoryNum'))
        map[combination] = {'n_artworks': 1, 'examples' : examples,'Acquired': row.get('Acquired'), 'Active': row.get('Active'), 'Status': row.get('Status'),}
    else:
        if len(map[combination]['examples']) < 7 and row.get('InventoryNum'):
            if row.get('InventoryNum') and row.get('InventoryNum').strip() != '':
                map[combination]['examples'].append(row.get('InventoryNum'))
        map[combination]['n_artworks'] += 1
    print len(map)

status_map = []
for item in map:
    map[item]['examples'] = ', '.join(map[item]['examples'])
    status_map.append(map.get(item))

rows_to_excel('./status_availability_map_python.xls', status_map, ['Acquired', 'Active', 'Status', '', 'n_artworks', 'examples', 'Artlogic Status', 'Artlogic Availability', '', 'artlogic-status', 'artlogic-availability'])


