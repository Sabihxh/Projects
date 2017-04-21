import os
import shutil
path_to_desktop = '../../'
list_of_folders = os.listdir(path_to_desktop)

# print list_of_folders
# print len(list_of_folders)

for file in list_of_folders:
    if file.endswith('.jpg'):
        shutil.move('%s/%s'%(path_to_desktop, file), '%s/images'%(path_to_desktop))
        print '.jpg images moved'

    elif 'Screen Shot' in file:
        shutil.move('%s/%s'%(path_to_desktop, file), '%s/screenshots'%path_to_desktop)
        print 'screen shots moved'

    elif file.endswith('.txt'):
        shutil.move('%s/%s'%(path_to_desktop, file), '%s/text_files'%(path_to_desktop))
        print '.jpg images moved'

    elif file.endswith('.sql'):
        shutil.move('%s/%s'%(path_to_desktop, file), '%s/SQL_files'%(path_to_desktop))
        print '.jpg images moved'

    elif file.endswith('.py'):
        shutil.move('%s/%s'%(path_to_desktop, file), '%s/python_files'%(path_to_desktop))
        print '.jpg images moved'

    elif file.endswith('.xls'):
        shutil.move('%s/%s'%(path_to_desktop, file), '%s/Excel_Files'%(path_to_desktop))
        print '.jpg images moved'