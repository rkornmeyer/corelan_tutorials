#!/usr/bin/python
'''
Created on Aug 20, 2014
@author: Peter Van Eeckhoutte
@author: superjokiman provided shellcode routine at http://blog.techorganic.com/2013/03/02/binary-to-shellcode/
@contact: http://www.corelan.be
@author: rjk
'''
import sys

if (len(sys.argv) == 1 or len(sys.argv) > 2):
    print ' usage: "python pveReadbin.py infile" '
    sys.exit()
print 'reading %s \n'%sys.argv[1]
ctr = 1
maxlen = 15
nullcount=0
shellcode = "\""
for b in open(sys.argv[1], "rb").read():
    shellcode += "\\x" + b.encode("hex")
    if b.encode("hex") == '00':
        nullcount+=1
    if ctr == maxlen:
        shellcode += "\" +\n\""
        ctr = 0
    ctr += 1
shellcode += "\""
print 'Read %d bytes '%len(open(sys.argv[1], "rb").read())
print shellcode
print 'Number of Null bytes: %d'%nullcount