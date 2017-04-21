from flpy.excel import sql_to_excel

sql_command_1 = """ SELECT
                    soldto,
                    soldtoid,
                    saledate,
                    firstName,
                    lastName,
                    email
                    FROM artworks art, fl_interactive_users fiu
                    WHERE YEAR(saledate) = 2015
                    AND art.soldtoid = fiu.id;
                """

sql_command_2 = """ SELECT
                    id,
                    firstname,
                    lastname
                    FROM
                    fl_interactive_users;
"""
sql_list_1 = [
    {
        'worksheet_title': 'ArtWork Sold in 2015',
        'sql': sql_command_1,
        'col_widths': {0: 4, 1: 2, 2: 3, 5: 6}
    },
    {
        'worksheet_title': 'fl_interactive_users',
        'sql': sql_command_2,
        'col_widths': {0: 2, 1: 5, 2: 5, 5: 6}
    }
]


sql_to_excel('bought_artwork.xls', 'aoldemo2', sql_list_1)
print('Created: bought_artwork.xls')



sql_command_4 = """ SELECT
        fl.firstname,
        ar.saledate,
        ac.price
        FROM 
        artworks ar
        INNER JOIN 
        accounts ac
        ON ac.soldtoid = ar.soldtoid
        INNER JOIN 
        fl_interactive_users fl
        ON ac.id = fl.id;     

    """








# sql_command_3 = """SELECT DISTINCT 
#     fl.lastname, 
#     a.soldtoid, 
#     c.price 
#     FROM artworks a 
#     INNER JOIN accounts c 
#     ON a.soldtoid = c.soldtoid 
#     INNER JOIN fl_interactive_users fl 
#     ON fl.id = c.id 
#     WHERE YEAR(a.saledate) = 2015 
#     GROUP BY a.soldtoid;"""




# sql_list_2 = [
#     {
#         'worksheet_title': 'ArtWork in 2015',
#         'sql': sql_command_2,
#         'col_widths': {0: 2, 1: 5, 2: 5}
#     }
# ]

# sql_list_2 = [
#     {
#         'worksheet_title': 'ArtWork in 2015',
#         'sql': sql_command_3,
#         'col_widths': {0: 2, 1: 2, 2: 5}
#     }
# ]









# fl.lastname,
# fl.directoryOrganisation,
# fl.email,
# fl.directoryTelephone,
# fl.categories