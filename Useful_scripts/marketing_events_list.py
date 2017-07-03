#!/opt/artlogic/bin/python

from aolpy.imports.artsystems.marketing_and_events_lists import *
from flpy.excel import convert_excel, rows_to_excel

class MyOverride(ArtSystemMarketingEventsListsImport):

    def __init__(self, sitename, encode_xml = False):
        self._sitename = sitename
        self._db_table = 'lists'
        self.encode_xml = encode_xml

        answer = raw_input('Do you need to clean list_items?')
        if answer == 'y':
             execute(self._sitename, """DELETE FROM list_items""")

        answer = raw_input('Do you need to create again?(marketing-and-events-lists-short.xls, marketing-and-events-lists-full.xls) ')
        if answer == 'y':
            
            print 'Generating relevant spreadsheets, please wait...'


            name_lists = []
            name_list_control =[]
            name_list_and_contact_list = []

            ## LISTS FROM CATEGORIES/TYPE (mggExport_Contacts.xls)
            contacts = convert_excel('./data/originals/contacts.xls')
          
            for contact in contacts.rows:
                columns = ['Content Narrative']
                for column in columns:
                    value = self._prep_text_field(contact, column)
                    if value:
                        items = value.split(';')
                        for item in items:
                            item = item.strip()
                            if item and item != '':
                                if item not in name_list_control:
                                    name_list_control.append(item)
                                    name_lists.append({'title': item})
                                name_list_and_contact_list.append({'importID': contact.get('ID'), 'Value': item})


            rows_to_excel('./data/originals/marketing-and-events-lists-short.xls', name_lists, ['title'])
            rows_to_excel('./data/originals/marketing-and-events-lists-full.xls', name_list_and_contact_list, ['importID','Value'])

        self._generate_import()

    def _set_filepaths(self):
        self._filepaths = [
            './data/originals/marketing-and-events-lists-short.xls',
            './data/out/%s-marketing-and-events-lists-no-empty.xls' % self._sitename,
            './data/out/%s-marketing-and-events-lists-final.xls' % self._sitename,
            './data/out/%s-marketing-and-events-lists.sql' % self._sitename,
            './data/out/%s-marketing-and-events-lists-original-stats.xls' % self._sitename,
            './data/out/%s-marketing-and-events-lists-result-stats.xls' % self._sitename
        ]

    def _checklist(self):
        answer = raw_input('Remove empty valuse from marketing & events lists? y to continue, other keys to skip')
        if answer == 'y':
            print 'Removing any blank values...'
            execute(self._sitename, """DELETE FROM lists WHERE title = '' """)
            print 'Completed'
        answer = raw_input('Sort out marketing & events lists? y to continue, other keys to skip')
        if answer == 'y':
            print 'Sorting out marketing & events lists...'
            marketingListFile = convert_excel('./data/originals/marketing-and-events-lists-full.xls')
            sort_out_imported_marketing_and_events_lists(self._sitename, marketingListFile)
            print 'Completed'
        print 'CHECKLIST:'
        print '1. Check marketing and event lists are matched to contacts'

    def _title(self, row):
        print row.get('title')
        return row.get('title')


    def _response_required(self, row):
        return 0


i = MyOverride('carlfreedman')