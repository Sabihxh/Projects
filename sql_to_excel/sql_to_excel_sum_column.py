from flpy.excel import sql_to_excel
database = 'aoldemo2'

sql_list = [
{
        'worksheet_title': 'All available artworks',
        'sql': "SELECT artist, title, retailPrice FROM artworks WHERE availability = 1 ORDER BY artist",
        'total_columns': [2],
        'totals_group_by_columns': [0]
    },
    {
        'worksheet_title': 'All on consignment artworks',
        'sql': "SELECT artist, title, retailPrice FROM artworks WHERE availability = 2 ORDER BY artist",
        'total_columns': [2],
        'totals_group_by_columns': [0]
    },
]
summary_sheet_config = {
    'worksheet_title':'MY COOL SUMMARY',
    'header_rows':['SUMMARY',"Summary sheet with the total retail price of artworks via artist"],
    'col_widths':{0:6,1:4},
    'custom_fieldtypes':{1:'financial'},
    'summary_column_headings':['Artist','Retail price totals'],
}
sql_to_excel(
    'Test_Expert.xls',
    database,
    sql_list,
    #include_summary_sheet=True,
    #summary_sheet_config=summary_sheet_config
)
print("Created -- Test_Expert")