import os
import shutil

INITIAL_FOLDER = os.path.abspath('./AS_DI')
FINAL_FOLDER = os.path.abspath('./all_images')

if not os.path.exists(FINAL_FOLDER):
	os.makedirs(FINAL_FOLDER)

def move_items(folder):
	for item in os.listdir(folder):
		if os.path.isdir(os.path.join(folder, item)):
			print "FOLDER: %s"%os.path.join(folder, item)
			move_items(os.path.join(folder, item))
		else:
			#shutil.move(os.path.join(folder, item),FINAL_FOLDER)
			shutil.copy(os.path.join(folder, item), os.path.join(folder,FINAL_FOLDER))
			print os.path.join(folder, item) + '   >>  ' + os.path.join(folder,FINAL_FOLDER)
move_items(INITIAL_FOLDER)