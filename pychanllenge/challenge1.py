#!/usr/bin/env python3.7
#http://www.pythonchallenge.com/pc/def/map.html
a="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
re=''
tmp="abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i in tmp:
        re+=chr((ord(i)-95)%26+97)
    else:
        re+=i
print(re)
print((ord('z')+2)%97+97)

print(a)