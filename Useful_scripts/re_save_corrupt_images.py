#!/opt/artlogic/bin/python

from flpy.files import filetype
import os
import imghdr
import shutil

rename = True
remove_extension = False
print_types = []
folder_paths = ['./data/images'] # , 'Artlogic transfer', 'images_euros'
types = []


for folder_path in folder_paths:
    images = os.listdir(folder_path)
    for image in images:

        image_type_info = filetype((os.path.join(folder_path, image)))
        image_type = '%s' % image_type_info.get('is_image')

        if image_type == 'jpeg':
            image_type = 'jpg'
        elif image_type == 'png':
            image_type = 'png'
        elif image_type == 'tiff':
            image_type = 'tiff'
        elif image_type == 'gif':
            image_type = 'gif'
        elif image_type == 'False' and image_type_info.get('mimetype') == 'application/octet-stream':
            image_type = 'pct'
        elif image_type == 'False' and image_type_info.get('mimetype') == 'application/pdf':
            image_type = 'pdf'
        elif image_type == 'False' and image_type_info.get('mimetype') == 'image/jpeg':
            image_type = 'jpg'
        else:
            print('*' * 10)
            print('OOPS')
            print image_type
            print image
            print filetype(os.path.join(folder_path,image))
            print('*' * 10)
            image_type = ''

        old_file_path = os.path.join(folder_path,image)
        new_image_name = image + '.' + image_type
        move_to_folder = './data/pictures-renamed/%s/'%image_type

        if image_type:
            if not os.path.exists(move_to_folder):
                os.makedirs(move_to_folder)
            if image_type != 'jpg':
                print '%s  ===>  %s'%(old_file_path, os.path.join(move_to_folder, new_image_name))
            shutil.copyfile(old_file_path, os.path.join(move_to_folder, new_image_name))






