#!/opt/artlogic/bin/python

"""No longer using this, use tiwanicontemporary to edit this"""


import os
from flpy.db.connection import execute
from aolpy.api.aol_images2_api import upload_image #https://docs.artlogic.net/developer_docs/ArtlogicOnline/imports/importing_images/
import time

class StandardImages2Import(object):

    def __init__(self):
        """Following are the things you can edit"""
        self._database = 'tiwanicontemporary'
        self.delimeter = ';'
        self._image_path = '/Users/artlogic/workspace/ArtlogicOnline/Artlogic-ImportScripts/2017/20170810-tiwanicontemporary/data/images'
        self.result = execute(self._database, "SELECT id, importedImageData FROM artworks where importedImageData <>''").rows
                
        self._answer = raw_input("Enter t to test, y to upload images, anything else to skip: ")
        self.images_in_folder = os.listdir(self._image_path) #This gets all images in images folder and puts it in list
        self._process_images()


    def _process_images(self):
        #Create id_image_map e.g. {id1: [imageA, imageB, ...], id2: [imageA, imageB, ...], ...}
        id_image_map = {row.get('id'):row.get('importedImageData').split(';') for row in self.result} 
        img_count = sum([len(x) for x in id_image_map.values()]) #This counts the total number of images to be uploaded

        print img_count

        if self._answer == 't':
            s_file = open('./data/out/images_success_log.txt', 'w')
            e_file = open('./data/out/images_error_log.txt', 'w')

            for _id, images in id_image_map.iteritems():
                for image in images:
                    if image in self.images_in_folder:
                        print True
                    else:
                        print False



    def _upload_images(self):
        pass



i = StandardImages2Import()

        

