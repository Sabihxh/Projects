import math
a_number = raw_input("Enter a poasitive number: ")
try:
    print math.sqrt(float(a_number))
except:
    print 'Inout was not valid'

print 'Still running'