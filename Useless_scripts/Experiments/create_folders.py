import os
import shutil

def main_directory(dir_name):
    if os.path.exists(dir_name):
        print True
    else:
        os.mkdir(dir_name)

def sub_directories():
    value = raw_input("How many folders do you want to create? ")
    for x in range(1, int(value) + 1):
        if os.path.exists('./test_directories/Test_%s'%x):
            print 'Test_%s already exists'%x 
        else:
            os.mkdir('./test_directories/Test_%s'%x)


def create_files():
    for x in range(1, 5):
        f = open('./test_directories/Test_%s/File_%s.txt'%(x, x), 'w')
        f.close()


def move_files():
    dir_list = os.listdir('./test_directories')
    for dirt in dir_list:
        if os.path.isdir('./test_directories/%s'%dirt):
            small_list = os.listdir('./test_directories/%s'%dirt)
            for x in small_list:
                if os.path.isfile('./test_directories/%s/%s'%(dirt, x)):
                    shutil.move('./test_directories/%s/%s'%(dirt, x), './move_it')
                    print 'Careful, its a hot file'
            print 'A pathetic folder'
        elif os.path.isfile('./test_directories/%s'%dirt):
            print 'about to move lol'
            shutil.move('./test_directories/%s'%dirt, './move_it')

# move_files()

def del_empty_dirs():
    for x in range(1, 5):
        if os.path.exists('./test_directories/Test_%s'%x):
            os.rmdir('./test_directories/Test_%s'%x) 



def del_full_dirs():
    answer = raw_input("Are you sure you want to delete non-empty folders? Y - to procede, else skip: ")
    if answer == 'Y':
        for x in range(1, 5):
            if os.path.exists('./test_directories/Test_%s'%x):
                shutil.rmtree('./test_directories/Test_%s'%x)


print os.path.join(os.path.sep, 'test_directories', 'Test_1')























