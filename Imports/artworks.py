from aolpy.imports.template.artworks import *
from flpy.db.connection import execute


class MyOverride(StandardInventoryImport):
    
    def _set_filepaths(self):
        self._filepaths = [
            './data/originals/artworks.xls', ## original spreadsheet
            './data/out/%s-inventory-no-empty.xls' % self._sitename, ## historic and not used
            './data/out/%s-artworks-final.xls' % self._sitename, ## final excel spreadsheet
            './data/out/%s-artworks.sql' % self._sitename, ## sql file generated from final excel spreadsheet
        ]

    def _importedImageData(self, row):
        result = self._prep_text_field(row, 'IMAGE ')
        return result

    def _location2(self, row):
        result = self._prep_text_field(row, 'OPTIONAL Gallery')
        return result

    def _notes(self, row):
        parts = []
        #columns = ['Notes', 'Made In']

        # result_Note = self._prep_text_field(row, 'Notes', preserveLineBreak = True)
        # result_Made = self._prep_text_field(row, 'Made In', preserveLineBreak = True)
        
        # result_Made_S = 'Made in: %s.' % result_Made

        # if result_Note and result_Made:
        #     parts.extend((result_Made_S, result_Note))

        # elif result_Note:
        #     parts.append(result_Note)

        # elif result_Made:
        #     parts.append(result_Made_S)

        value = self._prep_text_field(row, 'Notes', preserveLineBreak = True)
        if value:
            parts.append(value)
        value = self._prep_text_field(row, 'Made In', preserveLineBreak = True)
        if value:
            parts.append('Made in: %s.' % value)

        result = '\n'.join(parts)
        print result
        return result
        

i = MyOverride('practice')