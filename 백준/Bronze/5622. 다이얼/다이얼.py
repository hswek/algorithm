import sys
word=sys.stdin.readline().rstrip()
a=0
for i in word:
    if i=='A' or i =='B' or i=='C':
        a+=3
    if i=='D' or i =='E' or i=='F':
        a+=4
    if i=='G' or i =='H' or i=='I':
        a+=5
    if i=='J' or i =='K' or i=='L':
        a+=6
    if i=='M' or i =='N' or i=='O':
        a+=7
    if i=='P' or i =='Q' or i=='R' or i=='S':
        a+=8
    if i=='T' or i =='U' or i=='V':
        a+=9
    if i=='W' or i =='X' or i=='Y' or i=='Z':
        a+=10
print(a)