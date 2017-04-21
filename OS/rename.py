import os

a_list = os.listdir('./hello')
c = 1
for file in a_list:
    c += 1
    os.rename('./hello/%s' % file,'./hello/testing_%s.txt' % c)