from flpy.excel import convert_excel, rows_to_excel, strip_excel
import os
import shutil
from datetime import datetime as dt



def _delete_empty_columns():
    path_to_originals = '/Users/artlogic/workspace/ArtlogicOnline/Artlogic-ImportScripts/2017/02-20170503-MichaelHoppen/data/originals'
    original_paths = frozenset(x for x in os.listdir(path_to_originals) if x.endswith('.xls') or x.endswith('.xlsx'))
    output_folder = 'New_Spreadsheets_%s' % dt.now().strftime('%y%m%d_%H%M%S')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_path in original_paths:
        print 'Working on: %s' % file_path
        strip_excel(os.path.join(path_to_originals, file_path), os.path.join(output_folder, file_path))
        print "Completed: %s" % file_path
        print '***' * 20
        
def _information():
    pass

_delete_empty_columns()

