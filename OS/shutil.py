import shutil
import os
print os.getcwd()
print os.listdir('.')
print os.path.abspath('access.txt')
print os.path.abspath('./hello')
shutil.move('access.txt', './hello')
shutil.move(os.path.abspath('access.txt'), os.path.abspath('./hello'))

# multiple_files = []
# # abs_path = os.path.abspath('./hello')

# os.chdir('/Users/artlogic')
# files_in_downloads = os.listdir('./downloads')
# print os.getcwd()
# file = raw_input("Which spreadsheet would you like to move? ")
# # folder = raw_input("Where would you like to put this spreadsheet? ")

# for file_name in files_in_downloads:
#     if file in file_name:
#         multiple_files.append(file_name)

# print ', '.join(multiple_files)


# if len(multiple_files) >= 2:
#     file = raw_input("Enter the exact filename: ")
#     shutil.move(file, './Desktop/Test')

# elif len(multiple_files) == 1:
#     shutil.move(multiple_files[0], './Desktop/Test')

# for file_name in multiple_files:
#     if file == file_name:
#         print file_name