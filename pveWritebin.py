#!/usr/bin/python
'''
Created on Aug 20, 2014
@author: Original Author Peter Van Eeckhoutte
@contact: http://corelan.be
@author: rjk
'''
import sys
if (len(sys.argv) == 1 or len(sys.argv) > 2):
    print ' usage: "python pveWritebin.py outputfile" '
    sys.exit()

shellcode = { "You forgot to paste " +
             "your shellcode " +
             "In pveWritebin.py"}
count=0
print "Writing to " + sys.argv[1] + "\n"
binFile = open(sys.argv[1], 'wb+')
for byte in shellcode:
    binFile.write(byte)
binFile.close()
print "Wrote %d bytes to file \n" % len(byte)