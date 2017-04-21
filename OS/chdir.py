import os
path = '../'
Types_of_paths = """" ../ = down down a level by 1 from where you currently are
                    ./folder_name go up to the folder from current directory
                     """
retval = os.getcwd()
print 'Current working directory %s' % retval

os.chdir(path)

retval = os.getcwd()

print 'Directory changed to %s' % retval
