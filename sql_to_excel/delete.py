from flpy.excel import sql_to_excel


sql_command = ' SELECT id, artist from artworks limit 10;'

sql_list = [
    {
        'worksheet_title': 'artworks',
        'sql': sql_command,
        'data': None,
        'col_widths': {1: 5}
    }
]

sql_to_excel('delete.xls', 'aoldemo2', sql_list, user_friendly_fieldnames=True)

print 'Created: delete.xls'

