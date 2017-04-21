#!/opt/artlogic/bin/python
import os
from aolpy.imports.template.artworks import *



class MyOverride(StandardInventoryImport):

    def __init__(self, sitename, mode='live', encode_xml = False):
        self._sitename = sitename
        self._db_table = 'artworks'
        self.encode_xml = encode_xml
        self.image_file = os.listdir('./data/images')
        self._generate_import()

    def _import_source(self, row):
        return '21 Feb Import'

    def _importID(self, row):
        return '%s' % (row.get('ID') or '')

    def _importedArtworkTypes(self, row):
        return self._prep_text_field(row, 'Artwork Type')

    def _artist(self, row):
        return self._prep_text_field(row, 'Artist')

    def _purchaseDate(self, row):
        result = self._prep_text_field(row, 'Purchased date (for STOCK)')
        return result

    def _framed(self, row):
        result = 0
        if row.get('Framing details') and row.get('Framing details') != 'unframed':
            result = 1        
        return result

    def _currentOwner(self, row):
        return self._prep_text_field(row, 'Current Owner')

    def _purchasedFrom(self, row):
        result = []
        columns = ['Purchased from (for STOCK)', 'Custom 3']
        for column in columns:
            value = self._prep_text_field(row, column)
            if value and value != '':
                result.append(value)
        
        return '\n'.join(result)

    def _isEdition(self, row):
        result = 0
        value = self._prep_text_field(row, 'Is edition')  
        if value.lower() == 'yes':
            result = 1
        return result

    def _editionDetails(self, row):
        parts = []
        value = self._prep_text_field(row, 'Edition details')
        if value:
            parts.append(value)
        value = self._prep_text_field(row, 'Edition number')  
        if value:
            if len(parts):
                parts.append('(%s)' % value)
            else:
                parts.append(value)
        result = ' '.join(parts)
        return result

    def _purchasePrice(self, row):
        result = self._prep_text_field(row, 'Purchase  price (for STOCK)').replace(',', '')
        return result

    def _importedImageData(self, row):
        result = []
        value = '%s.jpg'%self._prep_text_field(row, 'Image filename')
        for image in self.image_file:
            if value == image:
                result.append(image)
        
        value = self._prep_text_field(row, 'Image filename')
        for image in self.image_file:
            if value in image:
                if '%s.jpg'%value != image and len('%s.jpgx'%value) == len(image):
                    if not image[-5].isdigit(): 
                        result.append(image)
        if result:
            return ';'.join(result)


    def _notes(self, row):
        result = self._prep_text_field(row, 'Quantity')
        if result and result != '':
            return 'Quantity: %s' % result

                
    def _show_secondary_images(self, row):
        return 1











i = MyOverride('vinylfactory')














