from aolpy.imports import *
from flpy.excel import excel_to_sql, convert_excel
from flpy.db.connection import execute
from flpy.utils import encode_sql
import time
import os

class CreateDataBaseFromSpreadsheets(BaseImport):

    def __init__(self, database, connected_tables=False):
        self._database = database
        self._connected_tables = connected_tables
        self.encode_xml = True
        self._set_filepaths()
        self._spreadsheet_folder = self._folderpaths[0]
        self._generate_database()
        if connected_tables:
            self._link_tables()

    def _set_filepaths(self):
        self._folderpaths = [
            './data/originals/',
        ]

    def _generate_database(self):
        create_all_tables = False
        answer = raw_input('Do you want to create the entire database?(y)')
        if answer == 'y':
            os.system('mysql -u root -e "DROP DATABASE IF EXISTS  %s"'%self._database)
            os.system('mysql -u root -e "CREATE DATABASE %s"'%self._database)
            create_all_tables = True

        for spreadsheet in os.listdir(self._spreadsheet_folder):
            if not spreadsheet.startswith('.') and not spreadsheet.startswith('~'):
                print spreadsheet
                if spreadsheet.endswith('.xls') or spreadsheet.endswith('.xlsx'):
                    table_name = spreadsheet.split('.')[0]
                    if not create_all_tables:
                       answer = raw_input('Do you want to create table_name?(y)')

                    if create_all_tables or answer == 'y':
                        rows = convert_excel(os.path.join(self._spreadsheet_folder, spreadsheet)).rows
                        if rows:
                            print 'CREATE TABLE `%s`'%table_name
                            execute(self._database , "DROP TABLE IF EXISTS  `%s`"%table_name)
                            fields = []
                            for key in rows[0].keys():
                                key = self._prep_key(key)
                                if key == 'id' or (key.startswith('rel') and key.endswith('Id')):
                                    fields.append("`%s` int NOT NULL DEFAULT 0"%key)
                                else:
                                    fields.append("`%s` text"%key)
                            statement = "CREATE TABLE `%s`(%s) ENGINE=MyISAM DEFAULT CHARSET=utf8"%(table_name, ', '.join(fields))
                            print statement
                            execute(self._database, statement)
                            time.sleep(2)
                            print "INSERTING DATA........"
                            for row in rows:
                                statement = "INSERT INTO %s SET  %s;"%(table_name, ', '.join(["`%s`='%s'"%(self._prep_key(key), encode_sql(self._prep_text_field(row, key, preserveLineBreak=True))) for key in row.keys()]))
                                execute(self._database, statement)


    def _prep_key(self, key):
        try:
            key = key.split('::')[1]
        except:
            pass
        return key

    def _link_tables(self):
        if self._connected_tables:
            for key, value in self._connected_tables.iteritems():
                main_table = ''
                linked_table = ''
                key_field_main = ''
                key_field_linked = ''
                main_table = key
                for key1, value1 in value.iteritems():
                    linked_table = key1
                    print "ADDING linkedID column to the linked table..."
                    execute(self._database, "ALTER TABLE %s ADD linkedID int" % linked_table)
                    key_field_main = value1[0]
                    key_field_linked = value1[1]
                print "LINKING main table to linked table...."
                execute(self._database,"UPDATE %s main, %s linked SET linked.linkedID = main.importID WHERE main.`%s`= linked.`%s`" % (main_table, linked_table, key_field_main, key_field_linked))






CreateDataBaseFromSpreadsheets('gavin_turk_source')
