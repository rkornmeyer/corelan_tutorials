'''
Created on Aug 18, 2014
@author: Original Author Peter Van Eeckhoutte
@author: rjk
'''
import sys
import binascii

if (len(sys.argv) == 1 or len(sys.argv) > 2):
    print 'usage: python pvePushString.py "String to put on the stack"' + "\n"
    sys.exit()

strToPush=sys.argv[1]
strThisChar=""
strThisHex=""
cnt=0
bytecnt=0
strHex=""
strOpcodes=""
strPush=""
print "String length : %d" % len(strToPush)
print "Opcodes to push this string onto the stack :\n\n"
while (cnt < len(strToPush)):
    strThisChar=strToPush[cnt:cnt+1]
    strThisHex="\\x" + binascii.hexlify(strThisChar)
    if (bytecnt < 3):
        strHex=strHex + strThisHex
        bytecnt=bytecnt + 1
    else:
        strPush=strHex + strThisHex
        strPush=strPush.translate(None,'\\x')
        strHex = "\\x68" + strHex + strThisHex + "    //PUSH 0x" + strPush[6:8] +strPush[4:6] + strPush[2:4] + strPush[0:2]
        strOpcodes=strHex + "\n" + strOpcodes
        strHex=""
        bytecnt=0
    cnt=cnt + 1
if (len(strHex) > 0):
    while (len(strHex) < 12 ):
        strHex = strHex + "\\x20"
    strPush = strHex
    strPush=strPush.translate(None,'\\x')
    strHex = "\\x68" + strHex + "\\x00" + "    //PUSH 0x00" + strPush[4:6] + strPush[2:4] + strPush[0:2]
    strOpcodes = strHex + "\n" + strOpcodes
else:
    strOpcodes="\\x68\\x20\\x20\\x20\\x00" + "    //PUSH 0x00202020" + "\n" + strOpcodes

print strOpcodes











