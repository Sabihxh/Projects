import os.path

print(os.path.exists('./hello/test.txt'))#True
print(os.path.exists('hello'))#True
print(os.path.exists('hellooooo'))#False
#returns the path of directory of a file
print(os.path.dirname('./hello/test.txt'))#./hello
#returns the full path of a file or directory
print(os.path.abspath('hello'))#/Users/artlogic/Desktop/PyProgs/OS/hello
#returns the name of the last folder or file in the path
print(os.path.basename('./hello/test.txt')) #test.txt

print os.listdir('./hello')
print os.getcwd() #prints current working directory