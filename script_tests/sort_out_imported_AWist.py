
from flpy.excel import slice_excel, excel_to_sql, convert_excel, rows_to_excel, strip_excel
from aolpy.sites import get_db
from flpy.db.connection import execute as _execute, get_mapping as _get_mapping
from flpy.utils import encode_sql, encode_xml

from aolpy.contacts import *




def sort_out_imported_artwork_lists(site, artworkListFile):
    outputFile = []
    execute = _execute
    print execute
    database = get_db(site)
    # Get a mapping of name to id from artwork_lists
    sql = "SELECT id, name FROM artwork_lists"
    result = execute(database, sql)
    if result:
        artworkListMap = {}
        for row in result.rows:
            ID = '%s' % (row.get('id') or '')
            name = '%s' % (row.get('name') or '')
            if ID and name:
                artworkListMap[name] = ID
        # Loop through artworkListFile to map all the id values
        # to the importID's
        importIDS = {}
        for row in artworkListFile.rows:
            importID = '%s' % (row.get('importID') or '')
            artworkList = '%s' % (row.get('Value') or '')
            if artworkList and importID:
                listId = '\r' + artworkListMap[artworkList]
                if importIDS.get(importID):
                    importIDS[importID] = importIDS[importID] + listId
                else:
                    importIDS[importID] = listId
        # Update artworks with the importID's and artworkListIDS we have
        # stored in importIDS
        for artwork in importIDS:
            importID = artwork
            artworkListIDS = importIDS[artwork]
            sql = "UPDATE artworks SET selected_artwork_lists = %s WHERE importID = %s"
            sdata = (artworkListIDS, importID)
            execute(database, sql, sdata)
            artworkListIDS = ', '.join(artworkListIDS)
            outputRow = {}
            outputRow['importID'], outputRow['artworkListIDS'] = importID, artworkListIDS
            outputFile.append(outputRow)
    rows_to_excel('data/out/artwork_lists_import.xls', outputFile,['importID', 'artworkListIDS'])
    print 'See data/out/artwork_lists_import.xls for a list of the artworks that were updated'



























