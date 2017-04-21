import os, sys

ret = os.access('access.txt', os.F_OK)
print('F_OK - return value %s ' % ret)

ret = os.access('access.txt', os.R_OK)
print('R_OK - return value %s' % ret)

ret = os.access('access.txt' , os.W_OK)
print(ret)

ret = os.access('access.txt', os.X_OK)
print ret