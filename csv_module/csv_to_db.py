import csv
import codecs
from flpy.db.connection import execute
from aolpy.imports import *

class CreateDataBaseFromSpreadsheets(BaseImport):    

    def __init__(self, database):
        self._database = database
        self.encode_xml = True
        self._set_filepaths()
        self.csv_to_db()

    def _set_filepaths(self):
        pass

    def csv_to_db(self):
        txt_file = r"./data/originals/EDITED_EXPORT_DECEMBER.txt"
        open_file = codecs.open(txt_file, encoding='utf-16')
        file_read = open_file.read()
        file_list = file_read.split('\r')
        headers = file_list[0].split('\t')
        fields = ["`%s` text" % x for x in headers]

        execute(self._database, "DROP TABLE IF EXISTS artworks")
        sql = "CREATE TABLE `artworks` (%s) ENGINE=MyISAM DEFAULT CHARSET=utf8" % (', '.join(fields))
        execute(self._database, sql)
        for line in file_list:
            if len(line) == 0: continue
            line_list = line.split('\t')
            encoded_line_list = [encode_sql(self._prep_text_field({'key': data}, 'key', preserveLineBreak=True)) for data in line_list]
            insert_sql = "INSERT INTO artworks SET %s;" %(', '.join(["`%s`='%s'" % (x, y) for x, y in zip(headers, encoded_line_list)]))
            execute(self._database, insert_sql)



i = CreateDataBaseFromSpreadsheets('juergan_teller')




