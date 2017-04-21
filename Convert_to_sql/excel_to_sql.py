from flpy.db.connection import execute
from flpy.excel import convert_excel
from flpy.utils import encode_sql, encode_xml

fioruccicollection = '../../../workspace/ArtlogicOnline/Artlogic-ImportScripts/2016/20161114-Fioruccicollection/data/originals/contacts_modified.xls'

for row in convert_excel(fioruccicollection).rows:
    print row.get('id')




