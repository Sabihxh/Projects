from flpy.utils import unique_id

from aolpy.sql.artwork import artwork_sql

#import sql_to_excel method from flpy.excel
from flpy.excel import sql_to_excel

#output_file = 'my-sql-test-%s.xls' % unique_id()
output_file = 'Testing.xls'

#Below is the list of sql commands
#sql_command = "SELECT id, stockNumber, artist, artistSort, title, artistSortTitleYear, Medium, Dimensions, signedAndDated, Provenance, Literature, Exhibitions, IF(isEdition = 1, 'YES', 'No') AS is_edition , editionDetails FROM artworks WHERE id BETWEEN 50 AND 55;"
sql_command_2 = "TRIM(IF(isEdition = 1, CONCAT_WS(' ', IF(editionDetails = '', NULL, CAST(editionDetails AS CHAR)),IF(editionMasterRecord = 0 AND editionID > 0,CONCAT('(', IF(editionArtistProofNumber > 0, 'AP ', IF(custom_edition_type_number > 0, CONCAT(custom_edition_type_id, ' '), '#')), IF(editionArtistProofNumber > 0, editionArtistProofNumber, IF(custom_edition_type_number > 0, custom_edition_type_number, CAST(editionNumber AS char))), IF(unlimited_edition, '', CONCAT('/', IF(editionArtistProofNumber > 0, editionArtistProofTotal, IF(custom_edition_type_total > 0, custom_edition_type_total, editionTotal)))), ')'), '')), NULL))"

sql_command = """SELECT 
    id, 
    stockNumber, 
    artist, 
    artistSort, 
    title, 
    artistSortTitleYear, 
    Medium, 
    Dimensions, 
    signedAndDated, 
    Provenance, 
    Literature, 
    Exhibitions,
    %s AS edition_details, 
    IF(isEdition = 1, 'YES', 'No') AS is_edition , 
    editionDetails 
    FROM 
    artworks 
    WHERE id BETWEEN 50 AND 55
""" % artwork_sql.edition_number_sql

#sql_to_excel(output_file, 'aoldemo2', sql_command)

sql_to_excel(output_file, 'aoldemo2', sql_command)


#print('Created export: %s' % output_file)
print("Created  export: %s" %output_file)
#sql_to_excel('pages.xls', 'my_database', 'SELECT * FROM accounts')
