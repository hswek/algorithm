import sys
from collections import deque

s=input()
boom=input()

d=deque()
def check_boom(d):
    if len(d)<len(boom):
        return False
    for i in range(1,len(boom)+1):
        if boom[-i]!=d[-i]:
            return False
    return True
def boomm(d):
    for i in range(len(boom)):
        d.pop()

for i in s:
    d.append(i)

    if check_boom(d)==True:
        #print('boom!')
        boomm(d)
    #print(d)
if len(d)==0:
    print('FRULA')
for i in d:
    print(i,end='')
                
    